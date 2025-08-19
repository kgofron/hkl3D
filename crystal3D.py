#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import argparse
from matplotlib.widgets import Slider, Button, TextBox
import math

# Comprehensive atomic radius data (in Angstroms)
# Data compiled from various sources including:
# - CRC Handbook of Chemistry and Physics
# - WebElements (webelements.com)
# - International Tables for Crystallography
ATOMIC_RADII = {
    # Alkali metals
    'Li': 1.52, 'Na': 1.86, 'K': 2.27, 'Rb': 2.48, 'Cs': 2.65, 'Fr': 2.80,
    
    # Alkaline earth metals
    'Be': 1.12, 'Mg': 1.60, 'Ca': 1.97, 'Sr': 2.15, 'Ba': 2.22, 'Ra': 2.23,
    
    # Transition metals - 3d series
    'Sc': 1.61, 'Ti': 1.45, 'V': 1.34, 'Cr': 1.28, 'Mn': 1.27, 'Fe': 1.26,
    'Co': 1.25, 'Ni': 1.24, 'Cu': 1.28, 'Zn': 1.39,
    
    # Transition metals - 4d series
    'Y': 1.78, 'Zr': 1.60, 'Nb': 1.46, 'Mo': 1.39, 'Tc': 1.36, 'Ru': 1.34,
    'Rh': 1.34, 'Pd': 1.37, 'Ag': 1.44, 'Cd': 1.49,
    
    # Transition metals - 5d series
    'Hf': 1.59, 'Ta': 1.46, 'W': 1.39, 'Re': 1.37, 'Os': 1.35, 'Ir': 1.36,
    'Pt': 1.39, 'Au': 1.44, 'Hg': 1.49,
    
    # Lanthanides
    'La': 1.87, 'Ce': 1.82, 'Pr': 1.82, 'Nd': 1.82, 'Pm': 1.81, 'Sm': 1.80,
    'Eu': 1.80, 'Gd': 1.80, 'Tb': 1.78, 'Dy': 1.77, 'Ho': 1.76, 'Er': 1.75,
    'Tm': 1.74, 'Yb': 1.94, 'Lu': 1.87,
    
    # Actinides
    'Ac': 1.88, 'Th': 1.80, 'Pa': 1.61, 'U': 1.55, 'Np': 1.55, 'Pu': 1.59,
    'Am': 1.73, 'Cm': 1.74, 'Bk': 1.70, 'Cf': 1.86, 'Es': 1.86, 'Fm': 1.86,
    'Md': 1.86, 'No': 1.86, 'Lr': 1.86,
    
    # Main group elements
    'B': 0.85, 'C': 0.70, 'N': 0.65, 'O': 0.60, 'F': 0.50, 'Ne': 0.38,
    'Al': 1.43, 'Si': 1.17, 'P': 1.10, 'S': 1.04, 'Cl': 0.99, 'Ar': 0.71,
    'Ga': 1.22, 'Ge': 1.22, 'As': 1.19, 'Se': 1.17, 'Br': 1.14, 'Kr': 1.03,
    'In': 1.63, 'Sn': 1.46, 'Sb': 1.46, 'Te': 1.47, 'I': 1.40, 'Xe': 1.24,
    'Tl': 1.70, 'Pb': 1.54, 'Bi': 1.54, 'Po': 1.68, 'At': 1.40, 'Rn': 1.34,
    
    # Other important elements
    'H': 0.31, 'He': 0.28
}

# Element colors for visualization (based on common conventions)
ELEMENT_COLORS = {
    # Metals
    'Li': '#CC80FF', 'Na': '#AB5CF2', 'K': '#8F40D4', 'Rb': '#9B4FDB', 'Cs': '#AC7E20', 'Fr': '#420D09',
    'Be': '#C2FF00', 'Mg': '#8AFF00', 'Ca': '#3DFF00', 'Sr': '#00FF00', 'Ba': '#00C754', 'Ra': '#00D452',
    'Sc': '#E6E6E6', 'Ti': '#BFC2C7', 'V': '#A6A6AB', 'Cr': '#8A99C7', 'Mn': '#9C7AC7', 'Fe': '#E06633',
    'Co': '#F090A0', 'Ni': '#50D050', 'Cu': '#C88033', 'Zn': '#7D80B0',
    'Y': '#94FFFF', 'Zr': '#94E0E0', 'Nb': '#73C2C9', 'Mo': '#54B5B5', 'Tc': '#3B9E9E', 'Ru': '#248F8F',
    'Rh': '#0A7D8C', 'Pd': '#006985', 'Ag': '#C0C0C0', 'Cd': '#FFD98F',
    'Hf': '#4DC2FF', 'Ta': '#4DA6FF', 'W': '#2194D6', 'Re': '#267DAB', 'Os': '#266696', 'Ir': '#175487',
    'Pt': '#D0D0E0', 'Au': '#FFD123', 'Hg': '#B8B8D0',
    
    # Non-metals
    'H': '#FFFFFF', 'He': '#D9FFFF', 'B': '#FFB5B5', 'C': '#909090', 'N': '#3050F8', 'O': '#FF0D0D',
    'F': '#90E050', 'Ne': '#B3E3F5', 'Al': '#BFA6A6', 'Si': '#F0C8A0', 'P': '#FF8000', 'S': '#FFFF30',
    'Cl': '#1FF01F', 'Ar': '#80D1E3', 'Ga': '#C28F8F', 'Ge': '#668F8F', 'As': '#BD80E3', 'Se': '#FFA100',
    'Br': '#A62929', 'Kr': '#5CB8D4', 'In': '#A67573', 'Sn': '#668080', 'Sb': '#9E63B5', 'Te': '#D47A00',
    'I': '#940094', 'Xe': '#429EB0', 'Tl': '#A6544D', 'Pb': '#575961', 'Bi': '#9E4FB5', 'Po': '#AB5C00',
    'At': '#754F45', 'Rn': '#428296',
    
    # Lanthanides and Actinides
    'La': '#70D4FF', 'Ce': '#FFC700', 'Pr': '#D9FFC7', 'Nd': '#C7FFC7', 'Pm': '#A3FFC7', 'Sm': '#8FFFC7',
    'Eu': '#61FFC7', 'Gd': '#45FFC7', 'Tb': '#30FFC7', 'Dy': '#1FFFC7', 'Ho': '#00FF9C', 'Er': '#00E675',
    'Tm': '#00D452', 'Yb': '#00BF38', 'Lu': '#00AB24',
    'Ac': '#70ABFA', 'Th': '#00BAFF', 'Pa': '#00A1FF', 'U': '#008FFF', 'Np': '#0080FF', 'Pu': '#006BFF',
    'Am': '#545CF2', 'Cm': '#785CE3', 'Bk': '#8A4FE3', 'Cf': '#A136D4', 'Es': '#B31FD4', 'Fm': '#B31FBA',
    'Md': '#B30DA6', 'No': '#BD0D87', 'Lr': '#C70066'
}

def get_atomic_radius(element_symbol):
    """
    Extract element symbol and return its atomic radius.
    """
    # Extract element symbol (first letter + second letter if lowercase)
    element = ''.join(filter(str.isalpha, element_symbol))
    if element in ATOMIC_RADII:
        return ATOMIC_RADII[element]
    else:
        print(f"Warning: Unknown element '{element}', using default radius 1.0 Å")
        return 1.0

def get_element_color(element_symbol):
    """
    Extract element symbol and return its color.
    """
    element = ''.join(filter(str.isalpha, element_symbol))
    if element in ELEMENT_COLORS:
        return ELEMENT_COLORS[element]
    else:
        return '#808080'  # Default gray color

def create_sphere(center, radius, resolution=20):
    """
    Create a 3D sphere using triangulation.
    """
    # Generate spherical coordinates
    phi = np.linspace(0, 2 * np.pi, resolution)
    theta = np.linspace(0, np.pi, resolution)
    
    # Create meshgrid
    phi_grid, theta_grid = np.meshgrid(phi, theta)
    
    # Convert to Cartesian coordinates
    x = center[0] + radius * np.sin(theta_grid) * np.cos(phi_grid)
    y = center[1] + radius * np.sin(theta_grid) * np.sin(phi_grid)
    z = center[2] + radius * np.cos(theta_grid)
    
    # Flatten arrays
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_flat = z.flatten()
    
    # Create vertices array
    vertices = np.column_stack((x_flat, y_flat, z_flat))
    
    # Create triangular faces
    faces = []
    for i in range(resolution - 1):
        for j in range(resolution - 1):
            # Calculate indices for current grid cell
            idx1 = i * resolution + j
            idx2 = i * resolution + (j + 1)
            idx3 = (i + 1) * resolution + j
            idx4 = (i + 1) * resolution + (j + 1)
            
            # Add two triangles for each grid cell
            faces.append([idx1, idx2, idx3])
            faces.append([idx2, idx4, idx3])
    
    return vertices, faces

def calculate_optimal_scale_factor(atoms, target_overlap=0.1):
    """
    Calculate optimal scale factor to achieve target overlap ratio.
    """
    if len(atoms) < 2:
        return 1.0, {}
    
    # Find minimum interatomic distance
    min_distance = float('inf')
    for i, atom1 in enumerate(atoms):
        for j, atom2 in enumerate(atoms[i+1:], i+1):
            dx = atom1['x'] - atom2['x']
            dy = atom1['y'] - atom2['y']
            dz = atom1['z'] - atom2['z']
            distance = math.sqrt(dx*dx + dy*dy + dz*dz)
            min_distance = min(min_distance, distance)
    
    # Calculate maximum radius sum
    max_radius_sum = 0
    for atom in atoms:
        radius = get_atomic_radius(atom['name'])
        max_radius_sum = max(max_radius_sum, radius)
    max_radius_sum *= 2  # For two atoms
    
    # Calculate optimal scale based on target overlap
    if max_radius_sum > 0:
        if target_overlap <= 0.0:
            # No overlap: scale so that scaled_radius_sum = min_distance
            optimal_scale = min_distance / max_radius_sum
        elif target_overlap >= 1.0:
            # Full overlap: scale so that scaled_radius_sum = 2 * min_distance
            optimal_scale = (2 * min_distance) / max_radius_sum
        else:
            # Partial overlap: scale so that scaled_radius_sum = min_distance * (1 + target_overlap)
            optimal_scale = (min_distance * (1 + target_overlap)) / max_radius_sum
    else:
        optimal_scale = 0.05  # Fallback for zero distance
    
    # Ensure scale factor is reasonable
    optimal_scale = max(0.01, min(1.0, optimal_scale))
    
    # Analyze overlap with optimal scale
    scaled_radius_sum = max_radius_sum * optimal_scale
    overlap_with_optimal = max(0, (scaled_radius_sum - min_distance) / scaled_radius_sum) if scaled_radius_sum > 0 else 0
    
    overlap_analysis = {
        'min_distance': min_distance,
        'max_radius_sum': max_radius_sum,
        'current_overlap_ratio': max(0, (max_radius_sum - min_distance) / max_radius_sum),
        'optimal_scale': optimal_scale,
        'overlap_with_optimal': overlap_with_optimal,
        'scaled_radius_sum': scaled_radius_sum,
        'target_overlap': target_overlap
    }
    
    return optimal_scale, overlap_analysis

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

def plot_atoms(atoms, scale_factor=1.0, show_bonds=False, bond_cutoff=2.5, 
               auto_scale=False, target_overlap=0.1, show_overlap_info=True,
               interactive=False):
    """
    Create an enhanced 3D plot of the crystal structure with atomic radii and interactive controls.
    
    Parameters:
    - atoms: List of atom dictionaries
    - scale_factor: Multiplier for atomic radii (default: 1.0)
    - show_bonds: Whether to show bonds between atoms (default: False)
    - bond_cutoff: Maximum distance for bond display in Angstroms (default: 2.5)
    - auto_scale: Whether to automatically calculate optimal scale factor (default: False)
    - target_overlap: Target overlap ratio for auto-scaling (default: 0.1)
    - show_overlap_info: Whether to display overlap analysis information (default: True)
    - interactive: Whether to add interactive scaling controls (default: False)
    """
    # Auto-scale if requested
    if auto_scale:
        optimal_scale, overlap_analysis = calculate_optimal_scale_factor(atoms, target_overlap)
        if show_overlap_info:
            print(f"\nOverlap Analysis:")
            print(f"  Minimum interatomic distance: {overlap_analysis['min_distance']:.3f} Å")
            print(f"  Maximum radius sum (scale 1.0): {overlap_analysis['max_radius_sum']:.3f} Å")
            print(f"  Current overlap ratio: {overlap_analysis['current_overlap_ratio']:.2%}")
            print(f"  Optimal scale factor: {optimal_scale:.3f}")
            print(f"  Overlap with optimal scale: {overlap_analysis['overlap_with_optimal']:.2%}")
        
        scale_factor = optimal_scale
        print(f"  Using auto-calculated scale factor: {scale_factor:.3f}")
    
    # Create figure and 3D axes
    if interactive:
        fig = plt.figure(figsize=(18, 14))
        ax = fig.add_subplot(111, projection='3d')
    else:
        fig = plt.figure(figsize=(16, 14))
        ax = fig.add_subplot(111, projection='3d')
    
    # Store original data for interactive updates
    original_atoms = atoms.copy()
    current_scale = scale_factor
    
    def update_plot(new_scale):
        """Update the plot with new scale factor"""
        nonlocal current_scale
        current_scale = new_scale
        
        # Clear the plot
        ax.clear()
        
        # Group atoms by element type
        element_groups = {}
        for atom in original_atoms:
            element = ''.join(filter(str.isalpha, atom['name']))
            if element not in element_groups:
                element_groups[element] = []
            element_groups[element].append(atom)
        
        # Plot atoms as 3D spheres with new scale
        all_spheres = []
        legend_elements = []
        
        for element, element_atoms in element_groups.items():
            if not element_atoms:
                continue
                
            # Get element properties
            radius = get_atomic_radius(element) * new_scale
            color = get_element_color(element)
            
            # Create spheres for all atoms of this element
            for atom in element_atoms:
                center = (atom['x'], atom['y'], atom['z'])
                vertices, faces = create_sphere(center, radius, resolution=15)
                
                # Create 3D polygon collection for the sphere
                sphere = Poly3DCollection([vertices[face] for face in faces], 
                                        alpha=0.8, facecolor=color, edgecolor='black', linewidth=0.5)
                ax.add_collection3d(sphere)
                all_spheres.append(sphere)
            
            # Add to legend
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor=color, markersize=10, 
                                            label=f'{element} (r={radius:.2f} Å)'))
        
        # Show bonds if requested
        if show_bonds:
            bond_lines = []
            for i, atom1 in enumerate(original_atoms):
                for j, atom2 in enumerate(original_atoms[i+1:], i+1):
                    # Calculate distance
                    dx = atom1['x'] - atom2['x']
                    dy = atom1['y'] - atom2['y']
                    dz = atom1['z'] - atom2['z']
                    distance = math.sqrt(dx*dx + dy*dy + dz*dz)
                    
                    # Check if atoms are close enough to form a bond
                    if distance <= bond_cutoff:
                        # Get atomic radii
                        r1 = get_atomic_radius(atom1['name']) * new_scale
                        r2 = get_atomic_radius(atom2['name']) * new_scale
                        
                        # Check if atoms are actually touching (within 20% of sum of radii)
                        if distance <= 1.2 * (r1 + r2):
                            bond_lines.append([[atom1['x'], atom1['y'], atom1['z']],
                                             [atom2['x'], atom2['y'], atom2['z']]])
            
            # Plot bonds
            for bond in bond_lines:
                ax.plot([bond[0][0], bond[1][0]], 
                       [bond[0][1], bond[1][1]], 
                       [bond[0][2], bond[1][2]], 
                       'k-', linewidth=2, alpha=0.7)
        
        # Restore plot elements
        ax.set_xlabel('X (fractional coordinates)')
        ax.set_ylabel('Y (fractional coordinates)')
        ax.set_zlabel('Z (fractional coordinates)')
        
        # Set title with current scale
        title = f'Crystal Structure - Atomic Radii Scale: {new_scale:.3f}x'
        if auto_scale:
            title += f' (Auto-scaled, target overlap: {target_overlap:.1%})'
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Set equal aspect ratio
        ax.set_box_aspect([1, 1, 1])
        
        # Auto-adjust view limits
        all_x = [atom['x'] for atom in original_atoms]
        all_y = [atom['y'] for atom in original_atoms]
        all_z = [atom['z'] for atom in original_atoms]
        
        # Add padding for atomic radii
        max_radius = max([get_atomic_radius(atom['name']) * new_scale for atom in original_atoms])
        padding = max_radius + 0.1
        
        ax.set_xlim([min(all_x) - padding, max(all_x) + padding])
        ax.set_ylim([min(all_y) - padding, max(all_y) + padding])
        ax.set_zlim([min(all_z) - padding, max(all_z) + padding])
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Add scale factor information at top-left, aligned with status box
        if show_overlap_info:
            info_text = f'Scale Factor: {new_scale:.3f}x\n'
            info_text += f'Min Distance: {min(all_x):.3f} to {max(all_x):.3f}\n'
            info_text += f'Max Radius: {max_radius:.3f} Å'
            
            ax.text2D(0.05, 0.95, info_text, transform=ax.transAxes, fontsize=10,
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                      verticalalignment='top')
        
        # Add legend
        ax.legend(handles=legend_elements, loc='upper right')
        
        # Redraw
        fig.canvas.draw_idle()
    
    # Initial plot
    update_plot(scale_factor)
    
    # Add interactive controls if requested
    if interactive:
        # Adjust layout to make room for controls (left side and bottom)
        plt.subplots_adjust(left=0.15, bottom=0.15)
        
        # Create slider for scale factor at the bottom
        ax_scale = plt.axes([0.2, 0.05, 0.6, 0.03])
        scale_slider = Slider(
            ax=ax_scale, label='Atomic Radius Scale',
            valmin=0.01, valmax=1.0, valinit=scale_factor,
            valfmt='%.3f'
        )
        
        # Create vertical buttons on the left side (smaller size)
        ax_reset = plt.axes([0.02, 0.75, 0.10, 0.03])
        reset_button = Button(ax_reset, 'Reset')
        
        ax_auto = plt.axes([0.02, 0.70, 0.10, 0.03])
        auto_button = Button(ax_auto, 'Auto-Scale')
        
        ax_optimal = plt.axes([0.02, 0.65, 0.10, 0.03])
        optimal_button = Button(ax_optimal, 'Optimal')
        
        # Create status textbox between Scale Factor info and Reset button
        ax_status = plt.axes([0.02, 0.82, 0.12, 0.04])
        status_textbox = TextBox(ax_status, 'Status:', initial='Ready')
        
        # Connect controls
        def on_scale_change(val):
            update_plot(val)
            status_textbox.set_val(f'Scale: {val:.3f}x')
        
        def on_reset_click(event):
            scale_slider.set_val(1.0)
            status_textbox.set_val('Reset to 1.0x')
        
        def on_auto_click(event):
            if auto_scale:
                optimal_scale, _ = calculate_optimal_scale_factor(original_atoms, target_overlap)
                scale_slider.set_val(optimal_scale)
                status_textbox.set_val(f'Auto-scaled: {optimal_scale:.3f}x')
            else:
                status_textbox.set_val('Auto-scale not enabled')
        
        def on_optimal_click(event):
            optimal_scale, _ = calculate_optimal_scale_factor(original_atoms, 0.0)  # No overlap
            scale_slider.set_val(optimal_scale)
            status_textbox.set_val(f'Optimal (no overlap): {optimal_scale:.3f}x')
        
        scale_slider.on_changed(on_scale_change)
        reset_button.on_clicked(on_reset_click)
        auto_button.on_clicked(on_auto_click)
        optimal_button.on_clicked(on_optimal_click)
        
        # Initial status
        status_textbox.set_val(f'Initial scale: {scale_factor:.3f}x')
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_reflections(hkl_data, initial_size=50):
    """
    Create a 3D plot of the crystal reflections with enhanced interactive controls.
    """
    # Create figure and 3D axes with extra space for controls
    fig = plt.figure(figsize=(16, 14))
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
    colorbar = plt.colorbar(scatter, label='|Fc|²')
    
    # Set labels and title
    ax.set_xlabel('H')
    ax.set_ylabel('K')
    ax.set_zlabel('L')
    ax.set_title(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])
    
    # Add grid
    ax.grid(True)
    
    # Adjust layout to make room for controls
    plt.subplots_adjust(bottom=0.4)
    
    # HKL Range Control Section
    # Extract H, K, L ranges
    h_min, h_max = min(h), max(h)
    k_min, k_max = min(k), max(k)
    l_min, l_max = min(l), max(l)
    intensity_min, intensity_max = min(sizes), max(sizes)
    
    # Create sliders for H, K, L ranges
    slider_height = 0.02
    slider_width = 0.3
    
    # H range sliders (min and max separately)
    h_min_slider_ax = plt.axes([0.1, 0.32, slider_width, slider_height])
    h_min_slider = Slider(h_min_slider_ax, 'H Min', h_min, h_max, valinit=h_min, valfmt='%d')
    
    h_max_slider_ax = plt.axes([0.1, 0.30, slider_width, slider_height])
    h_max_slider = Slider(h_max_slider_ax, 'H Max', h_min, h_max, valinit=h_max, valfmt='%d')
    
    # K range sliders (min and max separately)
    k_min_slider_ax = plt.axes([0.1, 0.26, slider_width, slider_height])
    k_min_slider = Slider(k_min_slider_ax, 'K Min', k_min, k_max, valinit=k_min, valfmt='%d')
    
    k_max_slider_ax = plt.axes([0.1, 0.24, slider_width, slider_height])
    k_max_slider = Slider(k_max_slider_ax, 'K Max', k_min, k_max, valinit=k_max, valfmt='%d')
    
    # L range sliders (min and max separately)
    l_min_slider_ax = plt.axes([0.1, 0.20, slider_width, slider_height])
    l_min_slider = Slider(l_min_slider_ax, 'L Min', l_min, l_max, valinit=l_min, valfmt='%d')
    
    l_max_slider_ax = plt.axes([0.1, 0.18, slider_width, slider_height])
    l_max_slider = Slider(l_max_slider_ax, 'L Max', l_min, l_max, valinit=l_max, valfmt='%d')
    
    # Intensity threshold slider
    intensity_slider_ax = plt.axes([0.1, 0.14, slider_width, slider_height])
    intensity_slider = Slider(intensity_slider_ax, 'Intensity Min', intensity_min, intensity_max, 
                            valinit=intensity_min, valfmt='%.2e')
    
    # Size factor slider (moved up)
    size_slider_ax = plt.axes([0.1, 0.10, slider_width, slider_height])
    size_slider = Slider(size_slider_ax, 'Size Factor', 1, 1000, valinit=initial_size)
    
    # Control buttons
    # Toggle visibility button
    toggle_ax = plt.axes([0.45, 0.28, 0.15, 0.05])
    toggle_button = Button(toggle_ax, 'Show All')
    
    # Reset ranges button
    reset_ranges_ax = plt.axes([0.45, 0.24, 0.15, 0.05])
    reset_ranges_button = Button(reset_ranges_ax, 'Reset Ranges')
    
    # Reset size button
    reset_size_ax = plt.axes([0.45, 0.20, 0.15, 0.05])
    reset_size_button = Button(reset_size_ax, 'Reset Size')
    
    # Clear filter button
    clear_ax = plt.axes([0.45, 0.16, 0.15, 0.05])
    clear_button = Button(clear_ax, 'Clear Filter')
    
    # Size presets
    preset_ax1 = plt.axes([0.65, 0.28, 0.12, 0.05])
    preset_ax2 = plt.axes([0.65, 0.24, 0.12, 0.05])
    preset_ax3 = plt.axes([0.65, 0.20, 0.12, 0.05])
    
    preset1 = Button(preset_ax1, '2x Max')
    preset2 = Button(preset_ax2, '3x Max')
    preset3 = Button(preset_ax3, '5x Max')
    
    # Status text box
    status_ax = plt.axes([0.65, 0.12, 0.3, 0.08])
    status_textbox = TextBox(status_ax, 'Status:', initial=f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
    
    # Store original data for filtering
    original_h = h.copy()
    original_k = k.copy()
    original_l = l.copy()
    original_sizes = sizes.copy()
    original_indices = np.arange(len(hkl_data))
    
    # Store colorbar reference to avoid overplotting
    current_colorbar = colorbar
    
    def update_display():
        """Update display based on current filter settings"""
        nonlocal current_colorbar
        
        # Get current range values
        h_min_val = h_min_slider.val
        h_max_val = h_max_slider.val
        k_min_val = k_min_slider.val
        k_max_val = k_max_slider.val
        l_min_val = l_min_slider.val
        l_max_val = l_max_slider.val
        intensity_threshold = intensity_slider.val
        size_factor = size_slider.val
        
        # Filter data based on ranges
        mask = ((original_h >= h_min_val) & (original_h <= h_max_val) &
                (original_k >= k_min_val) & (original_k <= k_max_val) &
                (original_l >= l_min_val) & (original_l <= l_max_val) &
                (original_sizes >= intensity_threshold))
        
        filtered_indices = original_indices[mask]
        
        # Remove existing colorbar to avoid overplotting
        if current_colorbar is not None:
            current_colorbar.remove()
        
        if len(filtered_indices) > 0:
            # Update scatter plot with filtered data
            h_filtered = original_h[filtered_indices]
            k_filtered = original_k[filtered_indices]
            l_filtered = original_l[filtered_indices]
            sizes_filtered = original_sizes[filtered_indices]
            
            # Calculate new sizes
            new_sizes = size_factor * (sizes_filtered / max_size)
            
            # Clear previous scatter plot and create new one
            ax.clear()
            
            # Recreate the scatter plot
            new_scatter = ax.scatter(h_filtered, k_filtered, l_filtered, 
                                   s=new_sizes, c=sizes_filtered, cmap='viridis', 
                                   alpha=0.6)
            
            # Create new colorbar
            current_colorbar = plt.colorbar(new_scatter, label='|Fc|²')
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {int(size_factor)})')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            # Update status
            status_textbox.set_val(f'Showing {len(filtered_indices)} reflections\nH: {h_min_val}-{h_max_val}, K: {k_min_val}-{k_max_val}, L: {l_min_val}-{l_max_val}\nIntensity ≥ {intensity_threshold:.2e}')
        else:
            # Clear scatter plot if no data matches
            ax.clear()
            current_colorbar = None
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Reflections Visualization\nNo reflections match criteria')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            status_textbox.set_val(f'No reflections match criteria\nH: {h_min_val}-{h_max_val}, K: {k_min_val}-{k_max_val}, L: {l_min_val}-{l_max_val}\nIntensity ≥ {intensity_threshold:.2e}')
        
        fig.canvas.draw_idle()
    
    def toggle_visibility(event):
        """Toggle between showing all data and filtered data"""
        nonlocal current_colorbar
        
        if toggle_button.label.get_text() == 'Show All':
            # Show filtered data
            toggle_button.label.set_text('Show Filtered')
            update_display()
        else:
            # Show all data
            toggle_button.label.set_text('Show All')
            
            # Remove existing colorbar to avoid overplotting
            if current_colorbar is not None:
                current_colorbar.remove()
            
            # Clear and recreate with all data
            ax.clear()
            
            # Recreate scatter plot with all data
            all_scatter = ax.scatter(original_h, original_k, original_l, 
                                   s=initial_sizes, c=original_sizes, cmap='viridis', 
                                   alpha=0.6)
            
            # Create new colorbar
            current_colorbar = plt.colorbar(all_scatter, label='|Fc|²')
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            status_textbox.set_val(f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
            fig.canvas.draw_idle()
    
    def reset_ranges(event):
        """Reset all range sliders to full range"""
        h_min_slider.set_val(h_min)
        h_max_slider.set_val(h_max)
        k_min_slider.set_val(k_min)
        k_max_slider.set_val(k_max)
        l_min_slider.set_val(l_min)
        l_max_slider.set_val(l_max)
        intensity_slider.set_val(intensity_min)
    
    def reset_size(event):
        """Reset size slider to initial value"""
        size_slider.set_val(initial_size)
    
    def clear_filter(event):
        """Clear all filters and show all data"""
        nonlocal current_colorbar
        
        reset_ranges(event)
        reset_size(event)
        toggle_button.label.set_text('Show All')
        
        # Remove existing colorbar to avoid overplotting
        if current_colorbar is not None:
            current_colorbar.remove()
        
        # Clear and recreate with all data
        ax.clear()
        
        # Recreate scatter plot with all data
        all_scatter = ax.scatter(original_h, original_k, original_l, 
                               s=initial_sizes, c=original_sizes, cmap='viridis', 
                               alpha=0.6)
        
        # Create new colorbar
        current_colorbar = plt.colorbar(all_scatter, label='|Fc|²')
        
        # Restore labels and title
        ax.set_xlabel('H')
        ax.set_ylabel('K')
        ax.set_zlabel('L')
        ax.set_title(f'Crystal Reflections Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
        
        # Restore grid and aspect ratio
        ax.grid(True)
        ax.set_box_aspect([1,1,1])
        
        # Restore HKL info text
        ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                  transform=ax.transAxes, fontsize=10, verticalalignment='top',
                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        status_textbox.set_val(f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
        fig.canvas.draw_idle()
    
    def set_preset_size(factor):
        def handler(event):
            size_slider.set_val(factor * max_size)
        return handler
    
    # Connect sliders and buttons
    h_min_slider.on_changed(lambda val: update_display())
    h_max_slider.on_changed(lambda val: update_display())
    k_min_slider.on_changed(lambda val: update_display())
    k_max_slider.on_changed(lambda val: update_display())
    l_min_slider.on_changed(lambda val: update_display())
    l_max_slider.on_changed(lambda val: update_display())
    intensity_slider.on_changed(lambda val: update_display())
    size_slider.on_changed(lambda val: update_display())
    
    toggle_button.on_clicked(toggle_visibility)
    reset_ranges_button.on_clicked(reset_ranges)
    reset_size_button.on_clicked(reset_size)
    clear_button.on_clicked(clear_filter)
    
    preset1.on_clicked(set_preset_size(2))
    preset2.on_clicked(set_preset_size(3))
    preset3.on_clicked(set_preset_size(5))
    
    # Add HKL info text on plot
    ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
              transform=ax.transAxes, fontsize=10, verticalalignment='top',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Show the plot
    plt.show()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Visualize crystal structure and reflections from HKL file with enhanced interactive controls')
    parser.add_argument('filename', help='Input HKL file')
    parser.add_argument('-m', '--mode', choices=['atoms', 'reflections'], default='atoms',
                      help='Visualization mode: atoms (crystal structure) or reflections (default: atoms)')
    parser.add_argument('-s', '--size', type=float, default=50.0,
                      help='Initial size factor for reflection spheres (default: 50.0)')
    
    # Enhanced crystal structure parameters
    parser.add_argument('--scale', type=float, default=1.0, 
                       help='Scale factor for atomic radii (default: 1.0)')
    parser.add_argument('-b', '--bonds', action='store_true', 
                       help='Show bonds between atoms')
    parser.add_argument('-c', '--cutoff', type=float, default=2.5,
                       help='Bond cutoff distance in Angstroms (default: 2.5)')
    parser.add_argument('-a', '--auto-scale', action='store_true',
                       help='Automatically calculate optimal scale factor to reduce overlapping')
    parser.add_argument('-o', '--overlap', type=float, default=0.1,
                       help='Target overlap ratio for auto-scaling (0.0-1.0, default: 0.1)')
    parser.add_argument('--no-overlap-info', action='store_true',
                       help='Hide overlap analysis information')
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Enable interactive atomic radius scaling controls')
    
    args = parser.parse_args()
    
    try:
        if args.mode == 'atoms':
            atoms = read_crystal_structure(args.filename)
            if not atoms:
                print("No atom data found in the file or incorrect format.")
                return
            plot_atoms(atoms, scale_factor=args.scale, 
                      show_bonds=args.bonds, bond_cutoff=args.cutoff,
                      auto_scale=args.auto_scale, target_overlap=args.overlap,
                      show_overlap_info=not args.no_overlap_info,
                      interactive=args.interactive)
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