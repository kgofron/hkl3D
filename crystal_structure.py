#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse

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

def plot_crystal_structure(atoms):
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
    ax.scatter(si_x, si_y, si_z, c='blue', marker='o', s=100, label='Si')
    
    # Plot O atoms
    o_x = [atom['x'] for atom in o_atoms]
    o_y = [atom['y'] for atom in o_atoms]
    o_z = [atom['z'] for atom in o_atoms]
    ax.scatter(o_x, o_y, o_z, c='red', marker='^', s=80, label='O')
    
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

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Read and visualize crystal structure from HKL file.')
    parser.add_argument('input_file', help='Path to the input HKL file')
    args = parser.parse_args()
    
    # Read and process the crystal structure
    atoms = read_crystal_structure(args.input_file)
    
    # Print the atomic positions
    print("\nCrystal Structure Data:")
    print("======================")
    print(f"Total number of atoms: {len(atoms)}")
    print("\nAtomic Positions (fractional coordinates):")
    print("Atom\tX\t\tY\t\tZ")
    print("-" * 40)
    
    for atom in atoms:
        print(f"{atom['name']}\t{atom['x']:.6f}\t{atom['y']:.6f}\t{atom['z']:.6f}")
    
    # Plot the crystal structure
    plot_crystal_structure(atoms)

if __name__ == "__main__":
    main() 