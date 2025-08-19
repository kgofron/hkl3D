# API Reference

This document provides detailed technical documentation for all functions, classes, and parameters in the HKL3D codebase.

## 📚 Python Modules

### hkl_reflections.py

The main module for HKL reflection visualization with interactive controls.

#### Functions

##### `read_hkl_file(filename)`
Reads HKL reflection data from a file.

**Parameters:**
- `filename` (str): Path to the HKL file

**Returns:**
- `list`: List of tuples containing (h, k, l, |Fc|²)

**Example:**
```python
hkl_data = read_hkl_file("EntryWithCollCode55782.hkl")
print(f"Loaded {len(hkl_data)} reflections")
```

##### `plot_crystal_structure(hkl_data, initial_size=50)`
Creates an interactive 3D visualization of HKL reflections.

**Parameters:**
- `hkl_data` (list): List of (h, k, l, |Fc|²) tuples
- `initial_size` (float): Initial size factor for spheres (default: 50.0)

**Features:**
- Interactive H, K, L range sliders
- Intensity threshold filtering
- Size factor adjustment
- Real-time display updates

**Returns:**
- `None`: Displays interactive matplotlib window

#### Interactive Controls

##### Range Sliders
- **H Min/Max**: Control H value range
- **K Min/Max**: Control K value range  
- **L Min/Max**: Control L value range
- **Intensity Min**: Filter by minimum intensity
- **Size Factor**: Adjust sphere sizes

##### Control Buttons
- **Show All/Show Filtered**: Toggle data display mode
- **Reset Ranges**: Restore full ranges
- **Reset Size**: Restore default size
- **Clear Filter**: Remove all filters

##### Size Presets
- **2x Max**: Double maximum size
- **3x Max**: Triple maximum size
- **5x Max**: Five times maximum size

### crystal_structure.py

Module for visualizing crystal structure from atomic positions.

#### Functions

##### `read_crystal_structure(filename)`
Reads atomic position data from HKL file.

**Parameters:**
- `filename` (str): Path to the HKL file

**Returns:**
- `list`: List of dictionaries containing atom information

**Atom Data Structure:**
```python
{
    'name': 'Si1',           # Atom name
    'x': 0.02000,           # X coordinate
    'y': 0.18960,           # Y coordinate  
    'z': 0.03800,           # Z coordinate
    'B': 0.00000,           # B-factor
    'occ': 1.00000,         # Occupancy
    'spin': 0.00000,        # Spin
    'charge': 0.00000       # Charge
}
```

##### `plot_crystal_structure(atoms)`
Creates 3D visualization of atomic positions.

**Parameters:**
- `atoms` (list): List of atom dictionaries

**Features:**
- 3D scatter plot of atomic positions
- Different markers for different atom types
- Interactive 3D navigation
- Coordinate axis display

### rotation_schematic.py

Module for generating diffractometer rotation axis diagrams.

#### Functions

##### `create_rotation_arrows(ax, center, radius=0.5, axis='z', color='blue', alpha=0.7)`
Creates rotation direction arrows around specified axis.

**Parameters:**
- `ax` (Axes3D): 3D matplotlib axes
- `center` (list): Center point [x, y, z]
- `radius` (float): Radius of rotation circle (default: 0.5)
- `axis` (str): Rotation axis ('x', 'y', or 'z', default: 'z')
- `color` (str): Arrow color (default: 'blue')
- `alpha` (float): Transparency (default: 0.7)

**Features:**
- Multiple arrows showing rotation direction
- Right-handed coordinate system
- Clear directional indicators

##### `plot_rotation_schematic()`
Creates complete rotation schematic diagram.

**Features:**
- All three rotation axes (ω, χ, φ)
- Color-coded coordinate system
- Rotation direction indicators
- Professional presentation layout

##### `main()`
Command-line interface for rotation schematic.

**Arguments:**
- `--save`: Save plot to file (e.g., rotation_schematic.png)

### crystal3D.py

Combined module providing both reflection and structure visualization.

#### Functions

##### `read_hkl_reflections(filename)`
Reads HKL reflection data (same as hkl_reflections.py).

##### `read_crystal_structure(filename)`
Reads crystal structure data (same as crystal_structure.py).

##### `plot_atoms(atoms)`
Visualizes atomic positions.

##### `plot_reflections(hkl_data, initial_size=50)`
Visualizes HKL reflections with size controls.

**Parameters:**
- `hkl_data` (list): List of (h, k, l, |Fc|²) tuples
- `initial_size` (float): Initial size factor (default: 50.0)

**Features:**
- Interactive size adjustment
- Size presets (2x, 3x, 5x Max)
- Reset functionality

##### `main()`
Command-line interface for combined functionality.

**Arguments:**
- `filename`: Input HKL file
- `-m, --mode`: Visualization mode ('atoms' or 'reflections')
- `-s, --size`: Initial size factor for spheres

## 🔧 C++ Components

### read_hkl.cpp

C++ program for reading and displaying HKL file contents.

#### Data Structures

##### `HKLData`
```cpp
struct HKLData {
    int h, k, l;           // Miller indices
    int multiplicity;       // Reflection multiplicity
    double dspacing;        // d-spacing in Angstroms
    double fc_squared;      // Structure factor squared
};
```

#### Functions

##### `has_hkl_extension(const std::string& filename)`
Checks if file has .hkl extension.

**Parameters:**
- `filename`: Input filename

**Returns:**
- `bool`: True if file has .hkl extension

##### `print_usage(const char* program_name)`
Displays program usage information.

##### `main(int argc, char* argv[])`
Main program entry point.

**Arguments:**
- `argc`: Argument count
- `argv`: Argument vector (expects HKL filename)

**Features:**
- HKL file parsing
- Data validation
- Tabular output
- Error handling

## 📊 Data Formats

### HKL File Structure

```
# TITLE  Crystal description
# CELL    a         b         c       alpha     beta      gamma
# SPCGRP  Space group information
#                    X         Y         Z         B         Occ       Spin      Charge
# Atom  Si1                    0.02000   0.18960   0.03800   0.00000   1.00000   0.00000   0.00000
# H   K   L     Mult    dspc                   |Fc|^2
   0    0    2     1      11.43050      0.69358575E+00
```

### Data Columns

1. **H, K, L**: Miller indices (integer)
2. **Mult**: Multiplicity (integer)
3. **dspc**: d-spacing in Angstroms (float)
4. **|Fc|^2**: Structure factor squared (float)

## 🎨 Visualization Parameters

### Matplotlib Settings

- **Figure Size**: 16x14 inches (HKL reflections), 12x10 inches (rotation schematic)
- **3D Projection**: Axes3D for all 3D visualizations
- **Colormap**: Viridis for intensity mapping
- **Alpha**: 0.6 for sphere transparency
- **Grid**: Enabled with alpha 0.3

### Color Scheme

- **X-axis (H)**: Red
- **Y-axis (K)**: Green
- **Z-axis (L)**: Blue
- **ω (Omega)**: Red arrows
- **χ (Chi)**: Green arrows
- **φ (Phi)**: Blue arrows

## 🔄 Interactive Features

### Slider Controls

All range sliders use matplotlib's `Slider` widget with:
- Real-time value updates
- Callback functions for display updates
- Proper event handling
- Value validation

### Button Controls

All buttons use matplotlib's `Button` widget with:
- Click event handling
- State management
- Visual feedback
- Consistent styling

### Text Display

Status information displayed using:
- `TextBox` widget for status updates
- `text2D` for plot annotations
- Real-time updates
- Read-only display

## 🚀 Performance Considerations

### Data Handling

- **Efficient Filtering**: NumPy boolean masking for fast data selection
- **Memory Management**: Proper cleanup of matplotlib objects
- **Update Optimization**: Minimal redraws during interactions

### Visualization

- **3D Rendering**: Optimized for typical HKL data sizes
- **Interactive Response**: Smooth slider and button interactions
- **Memory Usage**: Efficient scatter plot management

## 🐛 Error Handling

### File Operations

- **File Not Found**: Graceful error messages
- **Format Errors**: Validation of HKL file structure
- **Permission Issues**: Clear error reporting

### Data Validation

- **Missing Data**: Handling of incomplete records
- **Type Conversion**: Safe parsing of numerical values
- **Range Checking**: Validation of coordinate values

### User Interface

- **Slider Limits**: Dynamic range adjustment
- **Button States**: Proper state management
- **Display Updates**: Error handling during redraws

---

*Last updated: 2025*
