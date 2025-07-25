# 🌠 ASTROPHYSICS: Cosmic Code Toolkit by GUARDIANSOFCODE  

[![GitHub stars](https://img.shields.io/github/stars/GUARDIANSOFCODE/astrophysics?style=for-the-badge)](https://github.com/GUARDIANSOFCODE/astrophysics)  
[![GitHub forks](https://img.shields.io/github/forks/GUARDIANSOFCODE/astrophysics?style=for-the-badge)](https://github.com/GUARDIANSOFCODE/astrophysics/network)  
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blueviolet?style=for-the-badge&logo=python)](https://python.org)  

**GUARDIANSOFCODE presents** an astrophysics simulation suite that bridges theoretical cosmology with computational power. From event horizons to exoplanet atmospheres - all in Python.  

---

## 🪐 Key Features  
▸ **Galaxy Sandbox** - Smash Milky Way & Andromeda in 4K  
▸ **Gravitational Wave Visualizer** - LIGO-style chirp animations  
▸ **Exoplanet ATMOS** - Simulate TRAPPIST-1e's climate  
▸ **Cosmic Ray Tracer** - Follow particles from supernovae to Earth  
▸ **AI-Assisted Classification** - CNN models for galaxy morphology  

---

from goc_astrophysics import Supernova
sn = Supernova(mass=15, metallicity=0.02)  # Solar metallicity
sn.run_simulation()
sn.generate_lightcurve(observer_angle=45)  # View from 45°****























## 🚀 Installation  
```bash
# Clone with all submodules (includes sample datasets)
git clone --recurse-submodules https://github.com/GUARDIANSOFCODE/astrophysics.git

# Set up environment (requires conda)
conda env create -f environment.yml
conda activate astro-goc
