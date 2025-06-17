#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
from matplotlib.widgets import Slider, Button

def read_crystal_structure(filename):
    """
    Read crystal structure data from HKL file.
    Returns a list of dictionaries containing atom information.
    """
    atoms = []
    reading_atoms = False
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Check if we've reached the atom data section
            if 'X         Y         Z         B         Occ       Spin      Charge' in line:
                reading_atoms = True
                continue
            
            if reading_atoms and line.startswith('# Atom'):
                # Parse atom data
                parts = line.split()
                if len(parts) >= 10:  # Ensure we have all required fields
                    atom_data = {
                        'name': parts[2],
                        'x': float(parts[3]),
                        'y': float(parts[4]),
                        'z': float(parts[5]),
                        'B': float(parts[6]),
                        'occ': float(parts[7]),
                        'spin': float(parts[8]),
                        'charge': float(parts[9])
                    }
                    atoms.append(atom_data)
    
    return atoms

def read_hkl_reflections(filename):
    """
    Read HKL reflection data from HKL file.
    Returns a list of tuples containing (h, k, l, |Fc|²).
    """
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

def plot_atoms(atoms):
    """
    Create a 3D plot of the crystal structure with different markers for Si and O atoms.
    """
    # Create figure and 3D axes
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Separate Si and O atoms
    si_atoms = [atom for atom in atoms if atom['name'].startswith('Si')]
    o_atoms = [atom for atom in atoms if atom['name'].startswith('O')]
    
    # Plot Si atoms
    si_x = [atom['x'] for atom in si_atoms]
    si_y = [atom['y'] for atom in si_atoms]
    si_z = [atom['z'] for atom in si_atoms]
    ax.scatter(si_x, si_y, si_z, c='red', marker='s', s=100, label='Si')
    
    # Plot O atoms
    o_x = [atom['x'] for atom in o_atoms]
    o_y = [atom['y'] for atom in o_atoms]
    o_z = [atom['z'] for atom in o_atoms]
    ax.scatter(o_x, o_y, o_z, c='blue', marker='o', s=80, label='O')
    
    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Crystal Structure (Fractional Coordinates)')
    
    # Add legend
    ax.legend()
    
    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])
    
    # Show the plot
    plt.show()

def plot_reflections(hkl_data, initial_size=50):
    """
    Create a 3D plot of the crystal reflections with adjustable sphere sizes.
    """
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
    title = ax.set_title(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
    
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
        title.set_text(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {int(val)})')
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
    parser = argparse.ArgumentParser(description='Visualize crystal structure and reflections from HKL file')
    parser.add_argument('filename', help='Input HKL file')
    parser.add_argument('-m', '--mode', choices=['atoms', 'reflections'], default='atoms',
                      help='Visualization mode: atoms (crystal structure) or reflections (default: atoms)')
    parser.add_argument('-s', '--size', type=float, default=50.0,
                      help='Initial size factor for reflection spheres (default: 50.0)')
    
    args = parser.parse_args()
    
    try:
        if args.mode == 'atoms':
            atoms = read_crystal_structure(args.filename)
            if not atoms:
                print("No atom data found in the file or incorrect format.")
                return
            plot_atoms(atoms)
        else:  # reflections mode
            hkl_data = read_hkl_reflections(args.filename)
            if not hkl_data:
                print("No reflection data found in the file or incorrect format.")
                return
            plot_reflections(hkl_data, args.size)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

if __name__ == "__main__":
    main() 