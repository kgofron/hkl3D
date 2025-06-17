#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import re
import argparse
from matplotlib.widgets import Slider, Button

def read_hkl_file(filename):
    hkl_data = []
    found_header = False
    
    with open(filename, 'r') as f:
        for line in f:
            if "# H   K   L     Mult    dspc                   |Fc|^2" in line:
                found_header = True
                continue
            if found_header and line.strip() and not line.startswith('#'):
                # Parse the line
                values = line.split()
                if len(values) >= 6:
                    h, k, l = map(int, values[0:3])
                    fc_squared = float(values[5])
                    hkl_data.append((h, k, l, fc_squared))
    
    return hkl_data

def plot_crystal_structure(hkl_data, initial_size=50):
    # Create figure and 3D axes with extra space for sliders
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract coordinates and sizes
    h = np.array([x[0] for x in hkl_data])
    k = np.array([x[1] for x in hkl_data])
    l = np.array([x[2] for x in hkl_data])
    sizes = np.array([x[3] for x in hkl_data])
    
    # Store max_size for normalization
    max_size = np.max(sizes)
    
    # Calculate initial sizes
    initial_sizes = initial_size * (sizes / max_size)
    
    # Create scatter plot
    scatter = ax.scatter(h, k, l, 
                        s=initial_sizes,
                        alpha=0.6,
                        c=sizes,
                        cmap='viridis')
    
    # Add colorbar
    plt.colorbar(scatter, label='|Fc|²')
    
    # Set labels and title
    ax.set_xlabel('H')
    ax.set_ylabel('K')
    ax.set_zlabel('L')
    title = ax.set_title(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])
    
    # Add grid
    ax.grid(True)
    
    # Create slider for size adjustment
    slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])
    size_slider = Slider(slider_ax, 'Size Factor', 1, 1000, valinit=initial_size)
    
    def update_size(val):
        # Update scatter plot sizes
        new_sizes = val * (sizes / max_size)
        scatter.set_sizes(new_sizes)
        # Update title
        title.set_text(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {int(val)})')
        fig.canvas.draw_idle()
    
    # Register the update function with the slider
    size_slider.on_changed(update_size)
    
    # Add reset button
    reset_ax = plt.axes([0.8, 0.05, 0.1, 0.03])
    reset_button = Button(reset_ax, 'Reset')
    
    def reset_size(event):
        size_slider.reset()
    
    reset_button.on_clicked(reset_size)
    
    # Add size presets
    preset_ax1 = plt.axes([0.2, 0.10, 0.15, 0.03])
    preset_ax2 = plt.axes([0.4, 0.10, 0.15, 0.03])
    preset_ax3 = plt.axes([0.6, 0.10, 0.15, 0.03])
    
    preset1 = Button(preset_ax1, '2x Max')
    preset2 = Button(preset_ax2, '3x Max')
    preset3 = Button(preset_ax3, '5x Max')
    
    def set_preset_size(factor):
        def handler(event):
            size_slider.set_val(factor * max_size)
        return handler
    
    preset1.on_clicked(set_preset_size(2))
    preset2.on_clicked(set_preset_size(3))
    preset3.on_clicked(set_preset_size(5))
    
    # Show the plot
    plt.show()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Visualize crystal structure from HKL file')
    parser.add_argument('filename', help='Input HKL file')
    parser.add_argument('-s', '--size', type=float, default=50.0,
                      help='Initial size factor for spheres (default: 50.0)')
    
    args = parser.parse_args()
    
    try:
        hkl_data = read_hkl_file(args.filename)
        if not hkl_data:
            print("No data found in the file or incorrect format.")
            sys.exit(1)
        plot_crystal_structure(hkl_data, args.size)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 