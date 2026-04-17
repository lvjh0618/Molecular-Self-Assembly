# Molecular Dynamics Study: Self-Assembly of Herbal Small Molecules

## 📝 Overview
This repository hosts the computational workflow and methodology for my research on the supramolecular self-assembly of **two distinct herbal small molecules**. By employing advanced Molecular Dynamics (MD) simulations, I investigate the driving forces and kinetic pathways behind the formation of their nano-aggregates in aqueous environments.

This computational project is a core component of my MSc research at Nanjing Agricultural University, aiming to bridge traditional herbal pharmacology with modern computational biophysics for aquaculture disease control.

> **🔒 Data Privacy Note:** > To protect unpublished scientific findings, the specific identities of the two molecules and the complete 100ns production trajectories (`.xtc`/`.trr`) are maintained in a secure private environment pending formal publication. This public repository serves as a portfolio demonstrating the robust computational pipeline, parameterization protocols, and analytical scripts developed for this study.

## 🔬 Research Objectives
* **Pipeline Development:** Establish a highly reproducible, automated MD workflow from initial topology generation to trajectory post-processing.
* **Structural Analysis:** Quantify aggregation behavior through custom Python scripts, extracting key metrics (RMSD, Rg, SASA, and cluster size distribution).
* **Interaction Mechanism:** Characterize the non-covalent driving forces, specifically focusing on $\pi-\pi$ stacking and hydrophobic interactions that stabilize the self-assembled complexes.

## 🛠 Methodology & Technical Stack
* **Simulation Engine:** GROMACS (Force fields: OPLS-AA / GAFF)
* **Trajectory Analysis:** Custom Python scripts utilizing `MDAnalysis`, `MDTraj`, `pandas`, and `NumPy`
* **Data Visualization:** `Matplotlib` & `Seaborn` for statistical plotting; advanced `VMD` (Tcl scripting) and `PyMOL` for high-quality 3D molecular rendering
* **Version Control:** Git workflow for reproducible research

## 📂 Repository Architecture
The project is logically structured to mirror a standard Molecular Dynamics workflow:

```text
.
├── 01_System_Setup/          # Initial coordinates and topology generation protocols
├── 02_Protocols/             # Reproducible GROMACS parameters (em, nvt, npt, md)
├── 03_Scripts/               # Python & Shell scripts for automated trajectory analysis
├── 04_Visualization/         # VMD state files and rendering configurations
├── 05_Results/               # High-resolution plots (RMSD, Rg, SASA) and analytical outputs
├── requirements.txt          # Python environment dependencies
└── README.md                 # Project documentation

📈 Current Status
[√] Initial system setup and topology generation for both molecular systems.

[√] 100ns production runs completed under periodic boundary conditions.

[√] Post-simulation trajectory extraction and PBC correction.

[√] Quantitative data analysis (Clustering/H-Bonds/SASA) - In Progress.

## 👨‍🔬 About Me
**Jiahao Lv ** *MSc Student in Aquaculture, Nanjing Agricultural University*

**Research Interests:**
* **Computational Nanotechnology:** Molecular Dynamics (MD) simulations and supramolecular self-assembly.
* **Microbiology & Fish Immunology:** Understanding bacterial pathogenesis and host defense mechanisms in aquaculture.
* **Interdisciplinary Antimicrobial Strategies:** Bridging computational biophysics and nanomaterials to develop novel disease control solutions.

**Goal:** Aspiring to pursue a position-based PhD. I am deeply driven by cross-disciplinary research, aiming to leverage computational modeling and nanotechnology to solve real-world challenges in microbiology, immunology, and sustainable aquatic food systems.

📧 Contact: lvjh0618@163.com or leejia030618@gmail.com