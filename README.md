# Memetic Algorithm for WSN Coverage Optimization
Final Master's thesis project focused on optimizing coverage in Wireless Sensor Networks (WSNs) using a Memetic Algorithm.

This repository contains the implementation of a memetic algorithm for optimizing coverage in Wireless Sensor Networks (WSNs), as presented in my master's thesis.

The algorithm combines genetic algorithms with local search (hill climbing) to improve coverage connectivity and efficiency in 2D sensor networks.

### Problem Description
This project addresses the problem of sensor placement in a non-uniform 2D environment. The goal is to deploy sensors in a non-uniform 2D area such that:
- Full area coverage is achieved.
- All sensors form a connected network.
- Redundant or isolated sensors are avoided.

### Approach
- **Encoding:** Uses a binary or 2D position-based chromosome to represent sensor placements.
- **Global Optimization:** Employs a Genetic Algorithm (selection, crossover, mutation).
- **Local Refinement:** Applies Hill Climbing to fine-tune individual sensor positions.

### Requirements
- Python 3.9 or later
- NumPy
- Matplotlib (for visualizing coverage)

Install all dependencies with:
- pip install -r requirements.txt

### How to Run
Run the main simulation: python main.py

### Thesis Report
You can find the full thesis [here](report/memoire.pdf).

![language](https://img.shields.io/badge/language-Python-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![status](https://img.shields.io/badge/status-in%90progress-green)
![repo size](https://img.shields.io/github/repo-size/YOUR_USERNAME/YOUR_REPO)
![contributors](https://img.shields.io/github/contributors/YOUR_USERNAME/YOUR_REPO)

