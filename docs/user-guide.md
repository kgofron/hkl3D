# User Guide

This guide explains how to use the various tools and features of HKL3D for crystallographic data analysis and visualization.

## 🎯 Overview

HKL3D provides several tools for different aspects of crystallographic analysis:

- **HKL Reflections Visualization** - Interactive 3D plotting with range controls
- **Crystal Structure Display** - Atomic position visualization
- **Rotation Schematic** - Diffractometer axis diagrams
- **C++ Data Reader** - Command-line HKL file processing

## 🔍 HKL Reflections Visualization

### Basic Usage

The main tool for visualizing HKL reflection data is `hkl_reflections.py`:

```bash
python3 hkl_reflections.py your_file.hkl
```

### Features

#### Interactive Range Controls
- **H Range Sliders**: Control minimum and maximum H values
- **K Range Sliders**: Control minimum and maximum K values  
- **L Range Sliders**: Control minimum and maximum L values
- **Intensity Threshold**: Filter by minimum intensity value
- **Size Factor**: Adjust overall sphere sizes

#### Control Buttons
- **Show All/Show Filtered**: Toggle between all data and filtered view
- **Reset Ranges**: Restore full H, K, L ranges
- **Reset Size**: Restore default size factor
- **Clear Filter**: Remove all filters and show all data

#### Size Presets
- **2x Max**: Double the maximum size
- **3x Max**: Triple the maximum size
- **5x Max**: Five times the maximum size

### Example Workflow

1. **Load Data**: `python3 hkl_reflections.py EntryWithCollCode55782.hkl`
2. **Adjust H Range**: Use H Min/Max sliders to focus on specific H values
3. **Filter by Intensity**: Use Intensity Min slider to show only strong reflections
4. **Toggle View**: Click "Show Filtered" to see only selected reflections
5. **Adjust Size**: Use Size Factor slider or presets for better visibility

## 🏗️ Crystal Structure Visualization

### Basic Usage

View atomic positions from HKL files:

```bash
python3 crystal_structure.py your_file.hkl
```

### Features
- 3D visualization of atomic positions
- Different markers for different atom types
- Interactive 3D rotation and zoom
- Atomic coordinate display

## 🎪 Rotation Schematic

### Basic Usage

Generate diffractometer rotation axis diagrams:

```bash
python3 rotation_schematic.py
```

### Features
- **ω (Omega)**: X-axis rotation (red arrows)
- **χ (Chi)**: Y-axis rotation (green arrows)  
- **φ (Phi)**: Z-axis rotation (blue arrows)
- Right-handed coordinate system
- Clear rotation direction indicators

### Save Options

```bash
python3 rotation_schematic.py --save rotation_diagram.png
```

## 🔧 Combined Functionality

### Crystal3D Tool

The `crystal3D.py` script provides combined functionality:

```bash
# View reflections
python3 crystal3D.py -m reflections EntryWithCollCode55782.hkl

# View atomic structure
python3 crystal3D.py -m atoms EntryWithCollCode55782.hkl

# Custom size factor
python3 crystal3D.py -m reflections -s 100 EntryWithCollCode55782.hkl
```

### Options
- `-m, --mode`: Choose between 'atoms' or 'reflections'
- `-s, --size`: Set initial size factor for spheres

## 💻 C++ Data Reader

### Basic Usage

Read and display HKL file contents:

```bash
./read_hkl EntryWithCollCode176.hkl
```

### Features
- Parses HKL file format
- Displays reflection data in tabular format
- Shows H, K, L values, multiplicity, d-spacing, and intensity
- Command-line interface for scripting

## 📊 Understanding the Data

### HKL File Format

HKL files contain crystallographic reflection data:

```
# H   K   L     Mult    dspc                   |Fc|^2
   0    0    2     1      11.43050      0.69358575E+00
   2    0   -2     1       8.89791      0.74799341E+00
```

- **H, K, L**: Miller indices (integer values)
- **Mult**: Multiplicity
- **dspc**: d-spacing in Angstroms
- **|Fc|²**: Structure factor squared (intensity)

### Coordinate System

- **H**: Corresponds to X-axis (a* direction)
- **K**: Corresponds to Y-axis (b* direction)
- **L**: Corresponds to Z-axis (c* direction)
- **Right-handed**: Follows crystallographic conventions

## 🎨 Visualization Tips

### Best Practices

1. **Start with Full Range**: Begin with all data visible
2. **Use Intensity Filtering**: Focus on strong reflections first
3. **Adjust Size Gradually**: Use size controls for optimal visibility
4. **Combine Filters**: Use multiple range sliders together
5. **Save Views**: Use the save functionality for presentations

### Color Coding

- **Viridis Colormap**: Intensity values are color-coded
- **Sphere Sizes**: Proportional to reflection intensity
- **Alpha Transparency**: 0.6 for good visibility without clutter

## 🔄 Interactive Controls

### Mouse Controls

- **Left Click + Drag**: Rotate the 3D view
- **Right Click + Drag**: Zoom in/out
- **Middle Click + Drag**: Pan the view
- **Scroll Wheel**: Zoom in/out

### Keyboard Shortcuts

- **R**: Reset view to default orientation
- **H**: Toggle HKL info display
- **G**: Toggle grid display

## 📁 File Management

### Supported Formats

- **HKL Files**: Primary format for reflection data
- **CIF Files**: Can be converted to HKL using cif2hkl
- **Text Files**: Any text-based crystallographic data

### Data Sources

- **Neutron Scattering**: Primary target application
- **X-ray Diffraction**: Compatible data format
- **Synchrotron Data**: High-resolution measurements
- **Laboratory Sources**: Standard diffraction experiments

## 🚀 Advanced Features

### Batch Processing

Process multiple files:

```bash
for file in *.hkl; do
    python3 hkl_reflections.py "$file" &
done
```

### Custom Size Factors

```bash
# Large spheres for presentations
python3 hkl_reflections.py -s 200 your_file.hkl

# Small spheres for detailed analysis
python3 hkl_reflections.py -s 20 your_file.hkl
```

### Integration with Other Tools

```bash
# Convert CIF to HKL first
cif2hkl input.cif --output output.hkl

# Then visualize
python3 hkl_reflections.py output.hkl
```

## 🆘 Getting Help

### Common Questions

1. **No display appears**: Check matplotlib backend settings
2. **Sliders not working**: Ensure you're using the interactive matplotlib backend
3. **Performance issues**: Reduce data size or use more aggressive filtering
4. **File format errors**: Verify HKL file structure

### Support Resources

- Check the [Troubleshooting](troubleshooting.md) guide
- Review [Examples](examples.md) for usage patterns
- Consult the [API Reference](api-reference.md) for technical details

---

*Last updated: 2025*
