# API Reference

*Last updated: 2025*

This document provides detailed technical information about the functions, classes, and modules in the HKL3D project.

## Core Modules

### crystal3D.py

The main module providing comprehensive crystallographic visualization capabilities.

#### Main Functions

##### `read_crystal_structure(filename)`
Reads crystal structure data from HKL file.

**Parameters:**
- `filename` (str): Path to the HKL file

**Returns:**
- `list`: List of dictionaries containing atom information

**Atom Data Structure:**
```python
{
    'name': str,      # Atom name (e.g., 'Si1', 'O1')
    'x': float,       # X coordinate (fractional)
    'y': float,       # Y coordinate (fractional)
    'z': float,       # Z coordinate (fractional)
    'B': float,       # B-factor (thermal parameter)
    'occ': float,     # Occupancy
    'spin': float,    # Spin state
    'charge': float   # Charge
}
```

**Example:**
```python
atoms = read_crystal_structure('EntryWithCollCode176.hkl')
for atom in atoms:
    print(f"{atom['name']}: ({atom['x']:.3f}, {atom['y']:.3f}, {atom['z']:.3f})")
```

##### `read_hkl_reflections(filename)`
Reads HKL reflection data from HKL file.

**Parameters:**
- `filename` (str): Path to the HKL file

**Returns:**
- `list`: List of tuples containing (h, k, l, |Fc|²)

**Data Format:**
```python
[
    (h, k, l, intensity),  # h, k, l are integers, intensity is float
    ...
]
```

**Example:**
```python
reflections = read_hkl_reflections('EntryWithCollCode55782.hkl')
for h, k, l, intensity in reflections:
    print(f"HKL({h},{k},{l}): {intensity:.2e}")
```

##### `plot_atoms(atoms)`
Creates a 3D plot of the crystal structure.

**Parameters:**
- `atoms` (list): List of atom dictionaries from `read_crystal_structure()`

**Features:**
- Different markers for Si (red squares) and O (blue circles) atoms
- Interactive 3D navigation
- Equal aspect ratio for proper crystallographic proportions
- Professional layout suitable for publications

**Example:**
```python
atoms = read_crystal_structure('structure.hkl')
plot_atoms(atoms)
```

##### `plot_reflections(hkl_data, initial_size=50)`
Creates an enhanced 3D plot of crystal reflections with comprehensive interactive controls.

**Parameters:**
- `hkl_data` (list): List of reflection tuples from `read_hkl_reflections()`
- `initial_size` (float): Initial size factor for reflection spheres (default: 50.0)

**Enhanced Features:**

###### HKL Range Controls
- **H Min/Max Sliders**: Independent control of H value ranges
- **K Min/Max Sliders**: Independent control of K value ranges
- **L Min/Max Sliders**: Independent control of L value ranges
- **Real-time Updates**: Immediate visual feedback on range changes

###### Intensity and Size Controls
- **Intensity Threshold Slider**: Filter by minimum intensity value
- **Size Factor Slider**: Fine-tune sphere sizes (1x to 1000x)
- **Size Presets**: Quick size adjustments (2x Max, 3x Max, 5x Max)

###### Interactive Control Buttons
- **Show All/Show Filtered**: Toggle between complete and filtered datasets
- **Reset Ranges**: Restore full H, K, L ranges
- **Reset Size**: Return to initial size factor
- **Clear Filter**: Remove all filters and show complete dataset

###### Professional Interface
- **Large Display Area**: 16x14 inch figure for optimal viewing
- **Status Display**: Real-time status showing current filter settings
- **HKL Info Box**: On-plot information display
- **Organized Controls**: Logical control layout below the 3D plot

**Example:**
```python
reflections = read_hkl_reflections('reflections.hkl')
plot_reflections(reflections, initial_size=100)
```

#### Internal Functions

##### `update_display()`
Updates the 3D plot based on current filter settings.

**Features:**
- Filters data based on current slider values
- Recreates scatter plot to avoid overplotting issues
- Manages colorbar properly to prevent multiple colorbars
- Updates status display with current filter information

##### `toggle_visibility(event)`
Toggles between showing all data and filtered data.

**Features:**
- Switches button label between "Show All" and "Show Filtered"
- Recreates plot with appropriate dataset
- Maintains proper colorbar management

##### `reset_ranges(event)`
Resets all range sliders to their full range values.

##### `reset_size(event)`
Resets the size factor slider to the initial value.

##### `clear_filter(event)`
Clears all filters and shows the complete dataset.

##### `set_preset_size(factor)`
Creates a handler function for size preset buttons.

**Parameters:**
- `factor` (float): Size multiplier (e.g., 2.0 for 2x Max)

**Returns:**
- `function`: Event handler for the preset button

### rotation_schematic.py

Module for generating diffractometer rotation axis diagrams.

#### Main Functions

##### `create_rotation_arrows(ax, center, radius=0.5, axis='z', color='blue', alpha=0.7)`
Creates rotation arrows around a specified axis.

**Parameters:**
- `ax` (Axes3D): 3D axes object
- `center` (list): Center point [x, y, z]
- `radius` (float): Radius of rotation circle (default: 0.5)
- `axis` (str): Rotation axis ('x', 'y', or 'z')
- `color` (str): Arrow color (default: 'blue')
- `alpha` (float): Transparency (default: 0.7)

**Features:**
- Multiple arrows at different angles to show rotation direction
- Larger arrow at 3π/2 for emphasis
- Right-handed coordinate system compliance

##### `plot_rotation_schematic()`
Creates the complete rotation schematic.

**Features:**
- All three rotation axes (ω, χ, φ)
- Coordinate system arrows
- Rotation direction indicators
- Professional labeling and legend

### hkl_reflections.py

Module for HKL reflection visualization (legacy, now integrated into crystal3D.py).

#### Main Functions

##### `read_hkl_reflections(filename)`
Reads HKL reflection data (same as in crystal3D.py).

##### `plot_crystal_structure(atoms, scale_factor=1.0, show_bonds=False, bond_cutoff=2.5, auto_scale=False, target_overlap=0.1, show_overlap_info=True, interactive=False)`
Creates enhanced 3D plot of crystal structure with atomic radii and interactive controls.

**Parameters:**
- `atoms` (list): List of atom dictionaries with position and element information
- `scale_factor` (float): Multiplier for atomic radii (default: 1.0)
- `show_bonds` (bool): Whether to show chemical bonds (default: False)
- `bond_cutoff` (float): Maximum distance for bond detection in Angstroms (default: 2.5)
- `auto_scale` (bool): Whether to automatically calculate optimal scale factor (default: False)
- `target_overlap` (float): Target overlap ratio for auto-scaling (0.0-1.0, default: 0.1)
- `show_overlap_info` (bool): Whether to display overlap analysis information (default: True)
- `interactive` (bool): Whether to add interactive scaling controls (default: False)

**Features:**
- **3D Sphere Visualization**: True 3D spheres with realistic atomic radii
- **Smart Auto-Scaling**: Intelligent overlap reduction for optimal visibility
- **Interactive Controls**: Real-time atomic radius scaling with sliders and buttons (when interactive=True)
- **Professional Layout**: Organized interface with aligned information boxes and controls
- **Bond Visualization**: Chemical connectivity analysis and display
- **Element-Specific Colors**: Standard crystallographic color conventions

## Data Structures

### HKL Reflection Data
```python
reflection = (h, k, l, intensity)
# h, k, l: int - Miller indices
# intensity: float - |Fc|² value
```

### Atom Data
```python
atom = {
    'name': str,      # Atom identifier
    'x': float,       # X coordinate (fractional)
    'y': float,       # Y coordinate (fractional)
    'z': float,       # Z coordinate (fractional)
    'B': float,       # B-factor
    'occ': float,     # Occupancy
    'spin': float,    # Spin state
    'charge': float   # Charge
}
```

## Interactive Controls

### Slider Controls
All sliders provide real-time updates and use appropriate formatting:

- **H/K/L Range Sliders**: Integer formatting (`%d`)
- **Intensity Slider**: Scientific notation (`%.2e`)
- **Size Factor Slider**: Default float formatting

### Button Controls
All buttons include proper event handling and visual feedback:

- **Toggle Buttons**: Change label text to indicate current state
- **Reset Buttons**: Restore default values
- **Preset Buttons**: Apply predefined size factors

### Status Display
The status textbox provides continuous feedback on:
- Current reflection count
- Active HKL ranges
- Intensity threshold
- Filter status

## Error Handling

### File Reading
- Graceful handling of missing or malformed files
- Clear error messages for debugging
- Fallback behavior for incomplete data

### Data Validation
- Type checking for numerical values
- Range validation for slider limits
- Proper handling of empty datasets

### Plot Management
- Colorbar overplotting prevention
- Memory-efficient data filtering
- Proper cleanup of plot elements

## Performance Considerations

### Large Datasets
- Efficient NumPy array operations
- Smart filtering to reduce displayed data
- Memory-conscious plot updates

### Real-time Updates
- Optimized slider response
- Minimal redraw operations
- Efficient data masking

### Memory Management
- Proper cleanup of matplotlib objects
- Efficient data copying for filtering
- Colorbar management to prevent leaks

## Dependencies

### Required Packages
```python
import numpy as np                    # Numerical operations
import matplotlib.pyplot as plt       # Plotting
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting
from matplotlib.widgets import Slider, Button, TextBox  # Interactive controls
import argparse                       # Command-line interface
```

### Version Requirements
- **NumPy**: >= 1.19.0
- **Matplotlib**: >= 3.3.0
- **Python**: >= 3.7

## Command-Line Interface

### crystal3D.py
```bash
python3 crystal3D.py [options] filename

Options:
  -m, --mode {atoms,reflections}  Visualization mode (default: atoms)
  -s, --size FLOAT                 Initial size factor for reflections (default: 50.0)
  -h, --help                       Show help message
```

### rotation_schematic.py
```bash
python3 rotation_schematic.py [options]

Options:
  --save FILENAME                  Save plot to file
  -h, --help                      Show help message
```

## Integration Examples

### Custom Analysis Script
```python
from crystal3D import read_hkl_reflections, plot_reflections

# Load data
reflections = read_hkl_reflections('data.hkl')

# Custom filtering
strong_reflections = [r for r in reflections if r[3] > 1.0]

# Visualize
plot_reflections(strong_reflections, initial_size=75)
```

### Batch Processing
```python
import os
from crystal3D import read_hkl_reflections

# Process multiple files
for filename in os.listdir('.'):
    if filename.endswith('.hkl'):
        reflections = read_hkl_reflections(filename)
        print(f"{filename}: {len(reflections)} reflections")
```

This API provides comprehensive access to all the enhanced features of the HKL3D project, enabling both interactive use and programmatic integration.
