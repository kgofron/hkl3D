#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Slider, Button, TextBox
import argparse
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
    'H': 0.31, 'He': 0.28, 'Be': 1.12, 'B': 0.85, 'C': 0.70, 'N': 0.65,
    'O': 0.60, 'F': 0.50, 'Ne': 0.38, 'Al': 1.43, 'Si': 1.17, 'P': 1.10,
    'S': 1.04, 'Cl': 0.99, 'Ar': 0.71, 'Ga': 1.22, 'Ge': 1.22, 'As': 1.19,
    'Se': 1.17, 'Br': 1.14, 'Kr': 1.03, 'In': 1.63, 'Sn': 1.46, 'Sb': 1.46,
    'Te': 1.47, 'I': 1.40, 'Xe': 1.24, 'Tl': 1.70, 'Pb': 1.54, 'Bi': 1.54,
    'Po': 1.68, 'At': 1.40, 'Rn': 1.34
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

def read_crystal_structure(filename):
    """
    Read crystal structure data from HKL file.
    Returns a tuple of (atoms, lattice_params) where:
    - atoms: list of dictionaries containing atom information
    - lattice_params: dictionary with a, b, c, alpha, beta, gamma
    """
    atoms = []
    lattice_params = {}
    reading_atoms = False
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Parse lattice parameters from CELL line
            if line.startswith('# CELL'):
                parts = line.split()
                if len(parts) >= 7:
                    lattice_params = {
                        'a': float(parts[2]),
                        'b': float(parts[3]),
                        'c': float(parts[4]),
                        'alpha': float(parts[5]),
                        'beta': float(parts[6]),
                        'gamma': float(parts[7])
                    }
                    print(f"Lattice parameters: a={lattice_params['a']:.3f}, b={lattice_params['b']:.3f}, c={lattice_params['c']:.3f}")
                    print(f"Angles: α={lattice_params['alpha']:.2f}°, β={lattice_params['beta']:.2f}°, γ={lattice_params['gamma']:.2f}°")
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
    
    if not lattice_params:
        print("Warning: No lattice parameters found in file. Using default values.")
        lattice_params = {'a': 1.0, 'b': 1.0, 'c': 1.0, 'alpha': 90.0, 'beta': 90.0, 'gamma': 90.0}
    
    return atoms, lattice_params

def get_atomic_radius(element_symbol):
    """
    Get atomic radius for a given element symbol.
    Returns a default radius if element not found.
    """
    # Extract element symbol (remove numbers)
    element = ''.join(filter(str.isalpha, element_symbol))
    
    if element in ATOMIC_RADII:
        return ATOMIC_RADII[element]
    else:
        # Default radius for unknown elements
        print(f"Warning: Unknown element '{element}', using default radius 1.0 Å")
        return 1.0

def get_element_color(element_symbol):
    """
    Get color for a given element symbol.
    Returns a default color if element not found.
    """
    # Extract element symbol (remove numbers)
    element = ''.join(filter(str.isalpha, element_symbol))
    
    if element in ELEMENT_COLORS:
        return ELEMENT_COLORS[element]
    else:
        # Default color for unknown elements
        return '#808080'  # Gray

def convert_fractional_to_real(fractional_coords, lattice_params):
    """
    Convert fractional coordinates to real space coordinates using lattice parameters.
    
    Parameters:
    - fractional_coords: tuple of (x, y, z) fractional coordinates
    - lattice_params: dictionary with a, b, c, alpha, beta, gamma
    
    Returns:
    - real_coords: tuple of (x, y, z) real space coordinates in Angstroms
    """
    x_frac, y_frac, z_frac = fractional_coords
    a, b, c = lattice_params['a'], lattice_params['b'], lattice_params['c']
    alpha, beta, gamma = lattice_params['alpha'], lattice_params['beta'], lattice_params['gamma']
    
    # Convert angles to radians
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)
    gamma_rad = math.radians(gamma)
    
    # Calculate volume of unit cell
    V = a * b * c * math.sqrt(1 - math.cos(alpha_rad)**2 - math.cos(beta_rad)**2 - math.cos(gamma_rad)**2 + 
                                2 * math.cos(alpha_rad) * math.cos(beta_rad) * math.cos(gamma_rad))
    
    # Calculate reciprocal lattice parameters
    a_star = b * c * math.sin(alpha_rad) / V
    b_star = a * c * math.sin(beta_rad) / V
    c_star = a * b * math.sin(gamma_rad) / V
    
    # Calculate cosines of reciprocal angles
    cos_alpha_star = (math.cos(beta_rad) * math.cos(gamma_rad) - math.cos(alpha_rad)) / (math.sin(beta_rad) * math.sin(gamma_rad))
    cos_beta_star = (math.cos(alpha_rad) * math.cos(gamma_rad) - math.cos(beta_rad)) / (math.sin(alpha_rad) * math.sin(gamma_rad))
    cos_gamma_star = (math.cos(alpha_rad) * math.cos(beta_rad) - math.cos(gamma_rad)) / (math.sin(alpha_rad) * math.sin(beta_rad))
    
    # Convert fractional to real coordinates
    x_real = a * x_frac + b * math.cos(gamma_rad) * y_frac + c * math.cos(beta_rad) * z_frac
    y_real = b * math.sin(gamma_rad) * y_frac + c * (math.cos(alpha_rad) - math.cos(beta_rad) * math.cos(gamma_rad)) / math.sin(gamma_rad) * z_frac
    z_real = c * math.sin(beta_rad) * z_frac
    
    return (x_real, y_real, z_real)

def calculate_optimal_scale_factor(atoms, lattice_params, target_overlap=0.1):
    """
    Calculate optimal scale factor to reduce overlapping while maintaining visibility.
    
    Parameters:
    - atoms: List of atom dictionaries
    - lattice_params: Dictionary with lattice parameters
    - target_overlap: Target overlap ratio (0.0 = no overlap, 1.0 = full overlap)
    
    Returns:
    - optimal_scale: Recommended scale factor
    - overlap_analysis: Dictionary with overlap statistics
    """
    if len(atoms) < 2:
        return 1.0, {}
    
    # Calculate distances between all atom pairs in real space
    distances = []
    for i, atom1 in enumerate(atoms):
        for j, atom2 in enumerate(atoms[i+1:], i+1):
            # Convert fractional coordinates to real space
            real1 = convert_fractional_to_real((atom1['x'], atom1['y'], atom1['z']), lattice_params)
            real2 = convert_fractional_to_real((atom2['x'], atom2['y'], atom2['z']), lattice_params)
            
            # Calculate real space distance
            dx = real1[0] - real2[0]
            dy = real1[1] - real2[1]
            dz = real1[2] - real2[2]
            distance = math.sqrt(dx*dx + dy*dy + dz*dz)
            distances.append(distance)
    
    if not distances:
        return 1.0, {}
    
    # Get atomic radii
    radii = [get_atomic_radius(atom['name']) for atom in atoms]
    min_radius = min(radii)
    max_radius = max(radii)
    
    # Calculate current overlap with scale factor 1.0
    min_distance = min(distances)
    max_radius_sum = 2 * max_radius
    
    # Calculate optimal scale factor based on target overlap
    if min_distance > 0:
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
    optimal_scale = max(0.01, min(5.0, optimal_scale))
    
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

def create_sphere(center, radius, resolution=20):
    """
    Create a 3D sphere using triangulation.
    
    Parameters:
    - center: (x, y, z) coordinates of sphere center
    - radius: radius of the sphere
    - resolution: number of points for sphere generation (higher = smoother)
    
    Returns:
    - vertices: array of 3D points
    - faces: array of triangular faces
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

def plot_crystal_structure(atoms, lattice_params, scale_factor=1.0, show_bonds=False, bond_cutoff=2.5, 
                          auto_scale=False, target_overlap=0.1, show_overlap_info=True,
                          interactive=False):
    """
    Create a 3D plot of the crystal structure with atoms as 3D spheres.
    
    Parameters:
    - atoms: List of atom dictionaries
    - lattice_params: Dictionary with lattice parameters (a, b, c, alpha, beta, gamma)
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
        optimal_scale, overlap_analysis = calculate_optimal_scale_factor(atoms, lattice_params, target_overlap)
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
                # Convert fractional coordinates to real space
                real_center = convert_fractional_to_real((atom['x'], atom['y'], atom['z']), lattice_params)
                # Use higher resolution for smoother spheres
                vertices, faces = create_sphere(real_center, radius, resolution=25)
                
                # Create 3D polygon collection for the sphere
                sphere = Poly3DCollection([vertices[face] for face in faces], 
                                        alpha=0.8, facecolor=color, edgecolor='black', linewidth=0.3)
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
                    # Convert fractional coordinates to real space
                    real1 = convert_fractional_to_real((atom1['x'], atom1['y'], atom1['z']), lattice_params)
                    real2 = convert_fractional_to_real((atom2['x'], atom2['y'], atom2['z']), lattice_params)
                    
                    # Calculate real space distance
                    dx = real1[0] - real2[0]
                    dy = real1[1] - real2[1]
                    dz = real1[2] - real2[2]
                    distance = math.sqrt(dx*dx + dy*dy + dz*dz)
                    
                    # Check if atoms are close enough to form a bond
                    if distance <= bond_cutoff:
                        # Get atomic radii
                        r1 = get_atomic_radius(atom1['name']) * new_scale
                        r2 = get_atomic_radius(atom2['name']) * new_scale
                        
                        # Check if atoms are actually touching (within 20% of sum of radii)
                        if distance <= 1.2 * (r1 + r2):
                            bond_lines.append([real1, real2])
            
            # Plot bonds
            for bond in bond_lines:
                ax.plot([bond[0][0], bond[1][0]], 
                       [bond[0][1], bond[1][1]], 
                       [bond[0][2], bond[1][2]], 
                       'k-', linewidth=2, alpha=0.7)
        
        # Restore plot elements
        ax.set_xlabel('X (Å)')
        ax.set_ylabel('Y (Å)')
        ax.set_zlabel('Z (Å)')
        
        # Set title with current scale and lattice info
        title = f'Crystal Structure - Atomic Radii Scale: {new_scale:.3f}x'
        title += f'\na={lattice_params["a"]:.2f}Å, b={lattice_params["b"]:.2f}Å, c={lattice_params["c"]:.2f}Å'
        title += f', α={lattice_params["alpha"]:.1f}°, β={lattice_params["beta"]:.1f}°, γ={lattice_params["gamma"]:.1f}°'
        if auto_scale:
            title += f'\nAuto-scaled, target overlap: {target_overlap:.1%}'
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Auto-adjust view limits using real space coordinates
        all_real_coords = [convert_fractional_to_real((atom['x'], atom['y'], atom['z']), lattice_params) 
                          for atom in original_atoms]
        all_x = [coord[0] for coord in all_real_coords]
        all_y = [coord[1] for coord in all_real_coords]
        all_z = [coord[2] for coord in all_real_coords]
        
        # Add padding for atomic radii
        max_radius = max([get_atomic_radius(element) * new_scale for element in element_groups.keys()])
        padding = max_radius + 0.1
        
        # Calculate ranges for each axis
        x_range = max(all_x) - min(all_x)
        y_range = max(all_y) - min(all_y)
        z_range = max(all_z) - min(all_z)
        
        # Find the maximum range to ensure equal scaling
        max_range = max(x_range, y_range, z_range) + 2 * padding
        
        # Center the plot and set equal limits
        x_center = (min(all_x) + max(all_x)) / 2
        y_center = (min(all_y) + max(all_y)) / 2
        z_center = (min(all_z) + max(all_z)) / 2
        
        half_range = max_range / 2
        
        ax.set_xlim([x_center - half_range, x_center + half_range])
        ax.set_ylim([y_center - half_range, y_center + half_range])
        ax.set_zlim([z_center - half_range, z_center + half_range])
        
        # Set equal aspect ratio to maintain spherical appearance
        ax.set_box_aspect([1, 1, 1])
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Add scale factor information at top-left, aligned with status box
        if show_overlap_info:
            info_text = f'Scale Factor: {new_scale:.3f}x\n'
            info_text += f'Real Space Range:\n'
            info_text += f'X: {min(all_x):.2f} to {max(all_x):.2f} Å\n'
            info_text += f'Y: {min(all_y):.2f} to {max(all_y):.2f} Å\n'
            info_text += f'Z: {min(all_z):.2f} to {max(all_z):.2f} Å\n'
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
                optimal_scale, _ = calculate_optimal_scale_factor(original_atoms, lattice_params, target_overlap)
                scale_slider.set_val(optimal_scale)
                status_textbox.set_val(f'Auto-scaled: {optimal_scale:.3f}x')
            else:
                status_textbox.set_val('Auto-scale not enabled')
        
        def on_optimal_click(event):
            optimal_scale, _ = calculate_optimal_scale_factor(original_atoms, lattice_params, 0.0)  # No overlap
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

def print_atomic_info(atoms, lattice_params, scale_factor=1.0):
    """
    Print detailed atomic information including radii and scaling.
    """
    print("\nCrystal Structure Analysis:")
    print("=" * 60)
    print(f"Total number of atoms: {len(atoms)}")
    
    # Print lattice parameters
    print(f"\nLattice Parameters:")
    print("-" * 40)
    print(f"a = {lattice_params['a']:.3f} Å")
    print(f"b = {lattice_params['b']:.3f} Å")
    print(f"c = {lattice_params['c']:.3f} Å")
    print(f"α = {lattice_params['alpha']:.2f}°")
    print(f"β = {lattice_params['beta']:.2f}°")
    print(f"γ = {lattice_params['gamma']:.2f}°")
    
    # Group atoms by element
    element_counts = {}
    for atom in atoms:
        element = ''.join(filter(str.isalpha, atom['name']))
        if element not in element_counts:
            element_counts[element] = []
        element_counts[element].append(atom)
    
    print(f"\nElement composition:")
    print("-" * 40)
    for element, element_atoms in element_counts.items():
        radius = get_atomic_radius(element) * scale_factor
        print(f"{element:2s}: {len(element_atoms):2d} atoms, radius: {radius:.2f} Å (scaled)")
    
    print(f"\nAtomic Positions:")
    print("-" * 80)
    print("Atom\tFractional Coordinates\t\t\tReal Space (Å)\t\tRadius (Å)")
    print("\tX\t\tY\t\tZ\t\tX\t\tY\t\tZ")
    print("-" * 80)
    
    for atom in atoms:
        element = ''.join(filter(str.isalpha, atom['name']))
        radius = get_atomic_radius(element) * scale_factor
        real_coords = convert_fractional_to_real((atom['x'], atom['y'], atom['z']), lattice_params)
        print(f"{atom['name']:6s}\t{atom['x']:8.6f}\t{atom['y']:8.6f}\t{atom['z']:8.6f}\t"
              f"{real_coords[0]:8.2f}\t{real_coords[1]:8.2f}\t{real_coords[2]:8.2f}\t{radius:8.2f}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Enhanced crystal structure visualization with atomic radii and smart scaling.')
    parser.add_argument('input_file', help='Path to the input HKL file')
    parser.add_argument('-s', '--scale', type=float, default=1.0, 
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
    
    # Read and process the crystal structure
    atoms, lattice_params = read_crystal_structure(args.input_file)
    
    if not atoms:
        print("Error: No atomic data found in the file.")
        return
    
    # Print atomic information
    print_atomic_info(atoms, lattice_params, args.scale)
    
    # Plot the crystal structure
    plot_crystal_structure(atoms, lattice_params, scale_factor=args.scale, 
                          show_bonds=args.bonds, bond_cutoff=args.cutoff,
                          auto_scale=args.auto_scale, target_overlap=args.overlap,
                          show_overlap_info=not args.no_overlap_info,
                          interactive=args.interactive)

if __name__ == "__main__":
    main() 