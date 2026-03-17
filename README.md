# Gray-Scott Reaction-Diffusion Simulation

This repository contains a Python implementation of the **Gray-Scott model**, a mathematical system used to simulate the emergence of complex biological and chemical patterns—such as coral structures, zebrafish stripes, and bacterial growth—through reaction and diffusion.

## 📌 Project Significance
As a **Mathematical Engineering** student, I developed this project to explore how **Partial Differential Equations (PDEs)** and numerical methods can be translated into efficient code. This simulation demonstrates the bridge between abstract mathematical models and the biological complexity seen in nature.

## 🧬 The Mathematical Model
The simulation is governed by two coupled non-linear partial differential equations representing the concentration of two substances, $u$ and $v$:

$$\frac{\partial u}{\partial t} = D_u \nabla^2 u - uv^2 + f(1-u)$$
$$\frac{\partial v}{\partial t} = D_v \nabla^2 v + uv^2 - (f+k)v$$

### Parameters:
* **Diffusion Rates ($D_u, D_v$):** Control how quickly substances spread across the grid.
* **Feed Rate ($f$):** The rate at which substance $u$ is replenished.
* **Kill Rate ($k$):** The rate at which substance $v$ is removed from the system.

## 🛠 Engineering Implementation
* **Numerical Solving:** The Laplacian operator ($\nabla^2$) is computed using a discrete five-point stencil method implemented efficiently with `np.roll` for periodic boundary conditions.
* **Dynamic Visualization:** Real-time animation is generated using Matplotlib's `FuncAnimation` class, allowing users to observe pattern formation as the system evolves over time.
* **Pattern Presets:** The code includes predefined parameters to simulate specific biological patterns including **Coral**, **Zebrafish**, **Fingerprints**, and **Bacteria**.

## 📈 Connection to Deep Learning
This simulation serves as an excellent foundation for **Computer Vision** and **Convolutional Neural Networks (CNNs)**. The discrete Laplacian kernel used to compute diffusion is mathematically identical to the "filters" or "kernels" used in CNNs to detect edges and features in images. Understanding this link is pivotal for transitioning into high-level Deep Learning architectures.

## 🚀 Getting Started
1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   pip install numpy pandas matplotlib
