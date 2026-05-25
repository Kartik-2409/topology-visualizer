# 1D Convolution Boundary & Padding Visualizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://topology-visualizer-di9kaf4mkju5vqbidsa5ja.streamlit.app/])

### The Problem
In standard deep learning frameworks like PyTorch, applying a convolutional kernel over sequential data inherently drops boundary information (edge data) unless artificially preserved. This interactive tool visualizes the physical geometry of 1D convolutions, demonstrating exactly how stride length, kernel radius, and artificial padding dictate the final tensor dimensions.

![1D Convolution Visualizer App]([demo.png])

---

## 🧮 The Mathematical Formulation

The computational engine calculates the total number of valid operations (output patches) before applying the sliding window transformation. The boundary constraint is governed by the following floor function:

$$N = \left\lfloor \frac{L + 2P - K}{S} \right\rfloor + 1$$

Where the architectural parameters are defined as:
* $N$ = Total Output Patches (Resulting Tensor Dimension)
* $L$ = Sequence Length (Input Data Size)
* $P$ = Padding Magnitude (Zero-padding applied to boundaries)
* $K$ = Kernel Size (Receptive Field / Window Radius)
* $S$ = Stride (Step size of the convolutional jump)

By visualizing this operator, we can physically track how non-padded edges are mathematically ignored during the mapping process.

---

## ⚙️ Tech Stack & Architecture

This tool was built entirely in Python, bypassing standard frontend web frameworks to deploy mathematical logic directly to the cloud.

* **Core Logic & Matrices:** `NumPy`
* **Geometrical Plotting:** `Matplotlib`
* **Frontend UI & Deployment:** `Streamlit`
* **Theoretical Framework:** Applied Functional Analysis & Neural Network Operations

---

## 🚀 Run it Locally

If you wish to run the mathematical engine on your own machine:

1. Clone this repository:
```bash
git clone [https://github.com/Kartik-2409/topology-visualizer.git](https://github.com/Kartik-2409/topology-visualizer.git)
