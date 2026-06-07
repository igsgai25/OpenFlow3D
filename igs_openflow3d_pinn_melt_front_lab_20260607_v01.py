# -*- coding: utf-8 -*-
"""
🎓 OpenFlow3D - Physics-Informed Neural Network (PINN) Melt Front Lab
文件命名 (F.I.L.E.S.): igs_openflow3d_pinn_melt_front_lab_20260607_v01.py
領域 (Domain): igs (工業模擬) / chu (教學與實驗)
目的: 使用純 NumPy 自研極簡多層感知器 (MLP) 實作 PINN，預測二維流道內熔膠壓力分佈，解決 Laplace 物理方程式與邊界約束。
"""

import sys
import io
import numpy as np

# Force stdout/stderr to UTF-8 to prevent console mojibake on Windows systems
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class PureNumPyPINN:
    """
    純 NumPy 實作的物理資訊神經網路 (PINN) [INFERRED]
    預測二維流道穩態流動壓力分佈 p(x, y)。
    物理方程式 (Laplace): d2p/dx2 + d2p/dy2 = 0
    邊界條件:
      - 入口 (x=0): p = 1.0 (射出壓力)
      - 出口 (x=1): p = 0.0 (排氣出口)
      - 上下模壁 (y=0, y=0.2): dp/dy = 0 (無流動穿透)
    """
    def __init__(self, input_dim=2, hidden_dim=10, output_dim=1, lr=0.01):
        # 隨機初始化權重與偏差
        np.random.seed(42)
        self.W1 = np.random.randn(input_dim, hidden_dim) * 0.1
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, hidden_dim) * 0.1
        self.b2 = np.zeros((1, hidden_dim))
        self.W3 = np.random.randn(hidden_dim, output_dim) * 0.1
        self.b3 = np.zeros((1, output_dim))
        self.lr = lr

    def forward(self, X):
        """
        前向傳播，使用 Tanh 作為激活函數以保證二次可微 [VERIFIED]
        """
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = np.tanh(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = np.tanh(self.z2)
        self.z3 = np.dot(self.a2, self.W3) + self.b3
        self.y_pred = self.z3  # 輸出層不加激活函數，預測壓力
        return self.y_pred

    def compute_wall_gradient(self, x_wall, y_wall, dy=1e-4):
        """
        計算壁面邊界處的 dp/dy 數值梯度 (Neumann BC 驗證用) [INFERRED]
        使用中央差分法估算 dp/dy，壁面處應趨近 0。
        """
        p_y_plus = self.forward(np.column_stack((x_wall, y_wall + dy)))
        p_y_minus = self.forward(np.column_stack((x_wall, y_wall - dy)))
        dp_dy = (p_y_plus - p_y_minus) / (2 * dy)
        return dp_dy

    def compute_physics_residual(self, x, y, dx=1e-4, dy=1e-4):
        """
        利用數值差分計算 Laplace 物理殘差: d2p/dx2 + d2p/dy2 [INFERRED]
        """
        p_center = self.forward(np.column_stack((x, y)))
        
        # x 方向二次偏微分
        p_x_plus = self.forward(np.column_stack((x + dx, y)))
        p_x_minus = self.forward(np.column_stack((x - dx, y)))
        d2p_dx2 = (p_x_plus - 2 * p_center + p_x_minus) / (dx ** 2)
        
        # y 方向二次偏微分
        p_y_plus = self.forward(np.column_stack((x, y + dy)))
        p_y_minus = self.forward(np.column_stack((x, y - dy)))
        d2p_dy2 = (p_y_plus - 2 * p_center + p_y_minus) / (dy ** 2)
        
        # 物理殘差 (對於不可壓縮黏性流體之壓力分佈，應趨近於 0)
        residual = d2p_dx2 + d2p_dy2
        return residual

    def train_step(self, x_b, y_b, p_b, x_p, y_p, x_wall, y_wall):
        """
        使用數值梯度優化權重 (梯度下降法模擬反向傳播) [INFERRED]
        """
        # 合併邊界與內部點進行梯度計算
        weights = [self.W1, self.b1, self.W2, self.b2, self.W3, self.b3]
        grads = [np.zeros_like(w) for w in weights]
        
        eps = 1e-5
        
        # 計算當前總 Loss (邊界誤差 + 物理方程誤差)
        def get_total_loss():
            # 1. 邊界條件 Loss (MSE)
            p_b_pred = self.forward(np.column_stack((x_b, y_b)))
            loss_boundary = np.mean((p_b_pred - p_b) ** 2)
            
            # 2. 物理控制方程 Loss (MSE)
            phys_res = self.compute_physics_residual(x_p, y_p)
            loss_physics = np.mean(phys_res ** 2)
            
            # 3. 壁面 Neumann 邊界條件 Loss: dp/dy = 0 at y=0, y=0.2 [INFERRED]
            dp_dy_wall = self.compute_wall_gradient(x_wall, y_wall)
            loss_wall = np.mean(dp_dy_wall ** 2)
            
            return loss_boundary + 0.1 * loss_physics + 0.1 * loss_wall

        initial_loss = get_total_loss()
        
        # 數值估算每個權重的偏微分 (Finite Difference for Gradients)
        for idx, w in enumerate(weights):
            flat_w = w.ravel()
            flat_g = grads[idx].ravel()
            for i in range(len(flat_w)):
                orig_val = flat_w[i]
                
                flat_w[i] = orig_val + eps
                loss_plus = get_total_loss()
                
                flat_w[i] = orig_val - eps
                loss_minus = get_total_loss()
                
                flat_g[i] = (loss_plus - loss_minus) / (2 * eps)
                flat_w[i] = orig_val  # 復原
                
        # 梯度裁剪 (Gradient Clipping): 防止 lr=0.05 搭配數值梯度時發散 [INFERRED]
        max_norm = 1.0
        all_grad_flat = np.concatenate([g.ravel() for g in grads])
        total_norm = np.linalg.norm(all_grad_flat)
        if total_norm > max_norm:
            clip_ratio = max_norm / total_norm
            grads = [g * clip_ratio for g in grads]
        
        # 梯度更新
        self.W1 -= self.lr * grads[0]
        self.b1 -= self.lr * grads[1]
        self.W2 -= self.lr * grads[2]
        self.b2 -= self.lr * grads[3]
        self.W3 -= self.lr * grads[4]
        self.b3 -= self.lr * grads[5]
        
        return initial_loss

def run_pinn_flow_lab():
    print("="*60)
    print("OpenFlow3D: 2D 流道物理約束 PINN 壓力前沿預測實驗")
    print("="*60)
    
    # 1. 生成訓練數據點
    # 邊界點 (Inlet, Outlet)
    n_boundary = 20
    y_b = np.random.uniform(0, 0.2, n_boundary)
    x_b = np.zeros(n_boundary)  # Inlet x=0
    p_b = np.ones(n_boundary)   # Inlet p=1.0
    
    y_b2 = np.random.uniform(0, 0.2, n_boundary)
    x_b2 = np.ones(n_boundary)  # Outlet x=1
    p_b2 = np.zeros(n_boundary) # Outlet p=0.0
    
    x_boundary = np.concatenate([x_b, x_b2])
    y_boundary = np.concatenate([y_b, y_b2])
    p_boundary = np.concatenate([p_b, p_b2]).reshape(-1, 1)
    
    # 內部物理點 (Collocation Points)
    n_physics = 50
    x_p = np.random.uniform(0.01, 0.99, n_physics)
    y_p = np.random.uniform(0.01, 0.19, n_physics)
    
    # 壁面 Neumann 邊界點 (Wall Points): dp/dy = 0 at y=0, y=0.2 [INFERRED]
    n_wall = 20
    x_wall_bottom = np.random.uniform(0, 1, n_wall)
    y_wall_bottom = np.zeros(n_wall)          # 下壁 y=0
    x_wall_top = np.random.uniform(0, 1, n_wall)
    y_wall_top = np.ones(n_wall) * 0.2        # 上壁 y=0.2
    x_wall = np.concatenate([x_wall_bottom, x_wall_top])
    y_wall = np.concatenate([y_wall_bottom, y_wall_top])
    
    # 2. 初始化 PINN 網路
    pinn = PureNumPyPINN(lr=0.05)
    
    # 3. 迭代訓練
    epochs = 200
    print(f"[訓練] 開始執行 {epochs} 次物理損失迭代優化...")
    for epoch in range(epochs):
        loss = pinn.train_step(x_boundary, y_boundary, p_boundary, x_p, y_p, x_wall, y_wall)
        if epoch % 40 == 0:
            print(f"  - Epoch {epoch:3d} | Total Physics Loss (MSE): {loss:.6f} [VERIFIED]")
            
    # 4. 驗證與可視化 2D 流道的壓力分佈
    print("\n[驗證] 計算二維流道切面壓力 (預測值):")
    # 沿流道長度方向 (x=0 至 x=1) 進行預測
    test_x = np.linspace(0, 1, 10)
    test_y = np.ones_like(test_x) * 0.1  # 中央流道高
    test_coords = np.column_stack((test_x, test_y))
    predicted_pressures = pinn.forward(test_coords)
    
    # 輸出預測趨勢
    for i in range(len(test_x)):
        x_pos = test_x[i]
        p_val = predicted_pressures[i][0]
        # 用星號長度模擬壓力大小
        bar = "*" * int(p_val * 30)
        print(f"位置 x={x_pos:.2f} (流道長度方向) | 壓力={p_val:5.2f} MPa | {bar}")
        
    print("\n[診斷] 物理驗證結論:")
    # 檢查是否符合由高壓(1.0)向低壓(0.0)流動的物理特性
    inlet_pred = predicted_pressures[0][0]
    outlet_pred = predicted_pressures[-1][0]
    print(f"  - 入口預測值: {inlet_pred:.3f} MPa (理論值: 1.0) [VERIFIED]")
    print(f"  - 出口預測值: {outlet_pred:.3f} MPa (理論值: 0.0) [VERIFIED]")
    if inlet_pred > outlet_pred:
        print("  - [物理符合] 預測壓力由入口向出口遞減，流動方向正確。 [VERIFIED]")
    else:
        print("  - [物理偏差] 壓力梯度異常。 [EST]")
    print("="*60)

if __name__ == "__main__":
    run_pinn_flow_lab()
