# Memetic-WSN-Coverage-Optimization
Final Master's Thesis Project - Coverage Optimization in Wireless Sensor Networks using Memetic Algorithm.

This repository contains the implementation of a memetic algorithm for optimizing coverage in Wireless Sensor Networks (WSNs), as presented in my master's thesis.

The algorithm combines genetic algorithms with local search (hill climbing) to improve coverage connectivity and efficiency in 2D sensor networks.

### Problem Description
The goal is to deploy sensors in a non-uniform 2D area such that:
- Full area coverage is achieved.
- All sensors form a connected network.
- Redundant or isolated sensors are avoided.

### Approach
- **Encoding:** Binary/2D position-based chromosome.
- **Global Optimization:** Genetic Algorithm (selection, crossover, mutation).
- **Local Refinement:** Hill Climbing to adjust individual sensors locally.

### Requirements
- Python 3.9+
- NumPy
- Matplotlib (for plotting coverage results)

Install using: pip install -r requirements.txt

### How to Run
Run the main simulation: python main.py

### Thesis Report
You can find the full thesis [here](report/memoire.pdf).

#badges
![language](https://img.shields.io/badge/language-Python-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![status](https://img.shields.io/badge/status-in%20progress-yellow)
