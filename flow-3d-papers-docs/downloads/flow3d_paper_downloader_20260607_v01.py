# -*- coding: utf-8 -*-
"""
Flow in 3D - Top 30 Paper Downloader
Downloads open-access papers from arXiv and other sources.
"""
import os
import urllib.request
import ssl
import time
import json

DOWNLOAD_DIR = r"d:\L3-Academy\NCTU-Zack\flow-3d-papers-docs\downloads"
MANIFEST_PATH = os.path.join(DOWNLOAD_DIR, "download_manifest_20260607_v01.json")

# Top 30 papers to download - all open access (arXiv, PMC, NASA, etc.)
PAPERS = [
    # Theory 1: Navier-Stokes
    {"id": "paper_01", "arxiv": "2306.01776", "title": "From Zero to Turbulence - Generative Modeling for 3D Flow Simulation (ICLR 2024)", "theory": "T1+T5"},
    {"id": "paper_02", "arxiv": "2507.08972", "title": "Simulating 3D Turbulence with Physics-informed Neural Networks", "theory": "T1+T5"},
    {"id": "paper_03", "arxiv": "2210.07191", "title": "Stable nearly self-similar blowup of 2D Boussinesq and 3D Euler equations", "theory": "T1"},
    {"id": "paper_04", "arxiv": "2510.11220", "title": "A paradox concerning numerical simulation of Navier-Stokes turbulence", "theory": "T1"},
    {"id": "paper_05", "arxiv": "2509.08972", "title": "Discovery of Unstable Singularities in 3D Euler-NS equations", "theory": "T1"},

    # Theory 2: VOF & Free Surface
    {"id": "paper_06", "arxiv": "2012.12758", "title": "A review of Volume of Fluid methods for interface-resolving simulations", "theory": "T2"},
    {"id": "paper_07", "arxiv": "1811.12327", "title": "A coupled VOF-Level Set method for 3D unstructured meshes", "theory": "T2"},
    {"id": "paper_08", "arxiv": "2102.11403", "title": "Computational modeling of multiphase flows with surface tension", "theory": "T2"},

    # Theory 3: Turbulence Modeling
    {"id": "paper_09", "arxiv": "2301.12319", "title": "Machine learning for turbulence modeling and simulation advances in CFD", "theory": "T3"},
    {"id": "paper_10", "arxiv": "2105.02679", "title": "Machine learning accelerated computational fluid dynamics", "theory": "T3+T5"},
    {"id": "paper_11", "arxiv": "1906.02382", "title": "Turbulence modeling in the age of data - comprehensive review", "theory": "T3+T5"},
    {"id": "paper_12", "arxiv": "2004.05477", "title": "Learned discretizations for passive scalar advection in 2D turbulent flow", "theory": "T3+T5"},
    {"id": "paper_13", "arxiv": "1710.07313", "title": "Physics-informed machine learning for Reynolds stress modeling", "theory": "T3+T5"},

    # Theory 4: LBM, SPH, Meshfree
    {"id": "paper_14", "arxiv": "2106.12218", "title": "Grand challenges for SPH in computational fluid dynamics", "theory": "T4"},
    {"id": "paper_15", "arxiv": "2305.14514", "title": "Semi-Lagrangian Meshfree Lattice Boltzmann Method", "theory": "T4"},
    {"id": "paper_16", "arxiv": "2010.11929", "title": "Review of Lattice Boltzmann methods for multiphase flow", "theory": "T4"},
    {"id": "paper_17", "arxiv": "2502.17512", "title": "Learning multi-phase flow in fractured porous media with GNN", "theory": "T4+T5"},

    # Theory 5: AI-CFD (PINNs, Neural Operators)
    {"id": "paper_18", "arxiv": "1711.10561", "title": "Physics-informed neural networks (PINNs) - original paper by Raissi et al.", "theory": "T5"},
    {"id": "paper_19", "arxiv": "2010.08895", "title": "Fourier Neural Operator for parametric PDEs (FNO)", "theory": "T5"},
    {"id": "paper_20", "arxiv": "1910.03193", "title": "DeepONet - learning nonlinear operators", "theory": "T5"},
    {"id": "paper_21", "arxiv": "2202.11214", "title": "FourCastNet - global weather forecasting with adaptive FNO", "theory": "T5"},
    {"id": "paper_22", "arxiv": "2010.03957", "title": "Learning mesh-based simulation with graph networks (MeshGraphNets)", "theory": "T5"},
    {"id": "paper_23", "arxiv": "2002.07514", "title": "Learning to simulate complex physics with graph networks (GNS)", "theory": "T5"},
    {"id": "paper_24", "arxiv": "1806.01261", "title": "Relational inductive biases, deep learning, and graph networks", "theory": "T5"},
    {"id": "paper_25", "arxiv": "2209.15616", "title": "Towards multi-spatiotemporal-scale generalized PDE modeling", "theory": "T5"},
    {"id": "paper_26", "arxiv": "2310.02994", "title": "Multiple physics pretraining for physical surrogate models", "theory": "T5"},
    {"id": "paper_27", "arxiv": "2405.19101", "title": "Poseidon - efficient foundation models for PDEs", "theory": "T5"},
    {"id": "paper_28", "arxiv": "2306.00258", "title": "Neural operator survey - learning maps between function spaces", "theory": "T5"},
    {"id": "paper_29", "arxiv": "2111.05512", "title": "Physics-informed machine learning - Nature Reviews Physics", "theory": "T5"},
    {"id": "paper_30", "arxiv": "2209.12605", "title": "Recent advances in machine learning for computational fluid dynamics survey", "theory": "T5"},
]

def download_paper(paper, download_dir):
    """Download a paper from arXiv as PDF."""
    arxiv_id = paper["arxiv"]
    filename = f"{paper['id']}_{arxiv_id.replace('/', '_')}.pdf"
    filepath = os.path.join(download_dir, filename)

    if os.path.exists(filepath):
        return filepath, "already_exists"

    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (AEOS Research Bot; academic use)"
        })
        with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
            data = response.read()
            with open(filepath, "wb") as f:
                f.write(data)
        return filepath, "downloaded"
    except Exception as e:
        return filepath, f"error: {str(e)}"

def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    manifest = {
        "project": "Flow in 3D - PhD Research",
        "generated": "2026-06-07",
        "total_papers": len(PAPERS),
        "downloads": []
    }

    print(f"Starting download of {len(PAPERS)} papers...")
    print(f"Download directory: {DOWNLOAD_DIR}")
    print("-" * 60)

    success_count = 0
    for i, paper in enumerate(PAPERS):
        print(f"[{i+1:2d}/{len(PAPERS)}] Downloading: {paper['title'][:60]}...")
        filepath, status = download_paper(paper, DOWNLOAD_DIR)
        manifest["downloads"].append({
            "id": paper["id"],
            "arxiv_id": paper["arxiv"],
            "title": paper["title"],
            "theory": paper["theory"],
            "filepath": filepath,
            "status": status,
            "url": f"https://arxiv.org/abs/{paper['arxiv']}"
        })
        if "error" not in status:
            success_count += 1
            print(f"         -> {status}")
        else:
            print(f"         -> FAILED: {status}")

        # Rate limiting - be respectful to arXiv
        if i < len(PAPERS) - 1:
            time.sleep(3)

    # Save manifest
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("-" * 60)
    print(f"Download complete: {success_count}/{len(PAPERS)} successful")
    print(f"Manifest saved: {MANIFEST_PATH}")

if __name__ == "__main__":
    main()
