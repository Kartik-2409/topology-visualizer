import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="1D Convolution Visualizer", layout="wide")
st.title("The Boundary Problem: Convolution with & without Padding")

st.sidebar.header("Architecture Geometry")
sequence_length = st.sidebar.slider("Sequence Length", 10, 30, 16)
kernel_size = st.sidebar.slider("Kernel Size (Radius)", 1, 7, 3)
stride = st.sidebar.slider("Stride (Jump)", 1, 7, 2)
use_padding = st.sidebar.checkbox("Enable Padding (Save the Edge)", value=False)

padding_val = 1 if use_padding else 0

total_patches = int(np.floor((sequence_length + (2 * padding_val) - kernel_size) / stride)) + 1
st.sidebar.markdown(f"### Total Patches: {total_patches}")

fig, ax = plt.subplots(figsize=(10, 4))
ax.set_title(f"Kernel: {kernel_size} | Stride: {stride} | Padding: {padding_val}")

x_data = np.arange(1, sequence_length + 1)
y_data = np.zeros(sequence_length)
ax.scatter(x_data, y_data, color="black", s=100, label="Original Data")

if use_padding:
    ax.scatter([0], [0], color="red", marker="x", s=100, label="Left Padding")
    ax.scatter([sequence_length + 1], [0], color="red", marker="x", s=100, label="Right Padding")

start_pos = 0 if use_padding else 1
for i in range(total_patches):
    patch_start = start_pos + (i * stride)
    patch_end = patch_start + kernel_size - 1
    ax.plot([patch_start, patch_end], [-i - 1, -i - 1], linewidth=4, alpha=0.7)

ax.set_yticks([])
ax.legend()
st.pyplot(fig)
