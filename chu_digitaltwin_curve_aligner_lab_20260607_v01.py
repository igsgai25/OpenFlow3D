# -*- coding: utf-8 -*-
"""
🎓 Moldex3D Digital Twin - Cavity Pressure Curve Alignment Lab Helper
文件命名 (F.I.L.E.S.): chu_digitaltwin_curve_aligner_lab_20260607_v01.py
領域 (Domain): chu (教學與實驗)
目的: 模擬真實射出機台模穴壓力 (Physical Sensor) 與 Moldex3D 模擬結果 (Virtual Sim) 的曲線對齊與誤差校準。
"""

import sys
import io
import numpy as np

# Force stdout/stderr to UTF-8 to prevent console mojibake on Windows systems
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def generate_sensor_curves(timesteps=100):
    """
    生成模擬數據：真實機台壓力曲線 (帶雜訊與時間延遲) 與 Moldex3D 理論模擬壓力曲線 [INFERRED]
    """
    # 時間軸 (秒)
    t = np.linspace(0, 5, timesteps)
    
    # 1. Moldex3D 模擬理論壓力曲線 (無時間延遲，波形完美)
    # 模擬充填波峰與保壓平穩段
    sim_pressure = np.zeros_like(t)
    filling_mask = t <= 1.5
    packing_mask = (t > 1.5) & (t <= 3.5)
    cooling_mask = t > 3.5
    
    sim_pressure[filling_mask] = 80.0 * (t[filling_mask] / 1.5)**2
    sim_pressure[packing_mask] = 80.0 - 5.0 * (t[packing_mask] - 1.5)
    sim_pressure[cooling_mask] = (80.0 - 5.0 * 2.0) * np.exp(-1.5 * (t[cooling_mask] - 3.5))
    
    # 2. 真實機台壓力曲線 (延遲約 0.2 秒，且帶有機台高頻雜訊與系統誤差)
    delay_steps = 4
    noise = np.random.normal(0, 1.2, size=timesteps)
    physical_pressure = np.zeros_like(t)
    
    # 施加延遲與雜訊，波峰因系統熱損失略降 4%
    physical_pressure[delay_steps:] = sim_pressure[:-delay_steps] * 0.96
    physical_pressure = np.clip(physical_pressure + noise, 0, None)
    
    return t, sim_pressure, physical_pressure

def align_curves(t, sim_p, phys_p):
    """
    使用簡單的互相關 (Cross-correlation) 或峰值對齊演算法，估算並補償機台響應延遲 [INFERRED]
    """
    # 尋找兩條曲線的峰值索引
    sim_peak_idx = np.argmax(sim_p)
    phys_peak_idx = np.argmax(phys_p)
    
    # 計算延遲步長 (Lag steps)
    lag_steps = phys_peak_idx - sim_peak_idx
    time_step_size = t[1] - t[0]
    delay_time = lag_steps * time_step_size
    
    # 對齊曲線：將真實曲線向前平移 lag_steps 步長
    aligned_phys_p = np.zeros_like(phys_p)
    if lag_steps > 0:
        aligned_phys_p[:-lag_steps] = phys_p[lag_steps:]
        # 尾端用最後的值填充
        aligned_phys_p[-lag_steps:] = phys_p[-1]
    else:
        aligned_phys_p = np.copy(phys_p)
        
    return lag_steps, delay_time, aligned_phys_p

def calculate_rmse(y_true, y_pred):
    """
    計算均方根誤差 (RMSE) 以評估校準品質 [VERIFIED]
    """
    return np.sqrt(np.mean((y_true - y_pred)**2))

def run_calibration_analysis():
    print("="*60)
    print("Moldex3D 數位分身模穴壓力曲線對齊與校準實驗開跑...")
    print("="*60)
    
    # 1. 產生測試數據
    t, sim_p, phys_p = generate_sensor_curves(timesteps=100)
    
    # 2. 計算對齊前的原始誤差
    rmse_before = calculate_rmse(sim_p, phys_p)
    print(f"[狀態] 原始波形比對:")
    print(f"  - Moldex3D 模擬峰值壓力: {np.max(sim_p):.2f} MPa [VERIFIED]")
    print(f"  - 真實機台量測峰值壓力: {np.max(phys_p):.2f} MPa [VERIFIED]")
    print(f"  - 對齊前均方根誤差 (RMSE): {rmse_before:.2f} MPa [VERIFIED]")
    
    # 3. 執行虛實時間軸校準
    lag, delay, aligned_phys_p = align_curves(t, sim_p, phys_p)
    print(f"\n[對齊] 檢測到機台響應延遲:")
    print(f"  - 延遲步數: {lag} 步 [VERIFIED]")
    print(f"  - 估計響應時間延遲 (Response Delay): {delay:.3f} 秒 [VERIFIED]")
    
    # 4. 計算對齊後的校準誤差
    rmse_after = calculate_rmse(sim_p, aligned_phys_p)
    print(f"  - 對齊後均方根誤差 (RMSE): {rmse_after:.2f} MPa [VERIFIED]")
    
    # 5. 提供數位分身參數修正建議
    pressure_ratio = np.max(phys_p) / np.max(sim_p)
    viscosity_adjust = (pressure_ratio - 1.0) * 100.0
    print(f"\n[診斷] 數位分身反饋修正建議:")
    print(f"  - 壓力傳遞損耗比: {pressure_ratio:.2%} [VERIFIED]")
    print(f"  - 建議調整模流軟體中塑料黏度模型 (Cross-WLF Model) 黏度參數: {viscosity_adjust:.2f}% [INFERRED]")
    print(f"  - 時間對齊建議: 於 Moldex3D 射出成型機台介面中，設定延遲起跑時間為 {delay:.3f} 秒 [INFERRED]")
    print("="*60)
    
    # 輸出文字版簡單圖表
    print("\n[可視化] 壓力曲線趨勢簡易圖表 (ASCII Plot):")
    max_val = max(np.max(sim_p), np.max(phys_p))
    for i in range(0, 100, 10):
        t_val = t[i]
        # 理論壓力星號標示
        sim_stars = int((sim_p[i] / max_val) * 30)
        # 真實壓力井字標示
        phys_stars = int((phys_p[i] / max_val) * 30)
        
        sim_bar = "*" * sim_stars
        phys_bar = "#" * phys_stars
        print(f"t={t_val:.1f}s | Sim: {sim_bar:<30} | Phys: {phys_bar:<30}")

if __name__ == "__main__":
    run_calibration_analysis()
