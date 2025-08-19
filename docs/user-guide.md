# User Guide

*Last updated: 2025*

This guide explains how to use the various tools and features of the HKL3D project.

## Overview

The HKL3D project provides tools for visualizing and analyzing crystallographic data, including:
- Crystal structure visualization
- Reciprocal space (HKL) visualization with advanced filtering
- Rotation schematic generation
- Interactive 3D plots with real-time controls

## Crystal Structure Visualization

### Enhanced Crystal Structure Mode ⭐ **MAJOR UPDATE**

The crystal structure visualization has been **completely enhanced** with realistic atomic radii, 3D sphere rendering, and interactive controls.

#### Basic Usage

```bash
# Enhanced crystal structure visualization
python3 crystal3D.py -m atoms filename.hkl

# Interactive atomic radius scaling
python3 crystal3D.py -m atoms -i filename.hkl

# Auto-scaling for optimal visibility
python3 crystal3D.py -m atoms -a filename.hkl

# Full enhanced experience
python3 crystal3D.py -m atoms -a -b -i filename.hkl
```

#### Enhanced Features
- **3D Sphere Visualization**: True 3D spheres with realistic atomic radii (100+ elements)
- **Smart Auto-Scaling**: Intelligent overlap reduction for optimal visibility
- **Interactive Controls**: Real-time atomic radius scaling (0.01x to 1.0x)
- **Advanced Bond Visualization**: Chemical connectivity analysis and display
- **Element-Specific Colors**: Standard crystallographic color conventions
- **Professional Layout**: 18x14 inch display with organized controls
- **Overlap Control**: Configurable target overlap ratios (0.0 = no overlap, 1.0 = full overlap)
- **Lattice Parameter Integration**: Automatic reading of a, b, c, α, β, γ from .hkl files
- **Real Space Coordinates**: Plots atoms in true Angstrom coordinates instead of fractional
- **Accurate Crystallography**: Proper coordinate transformation for non-orthogonal systems
- **Spherical Appearance**: Maintains perfect sphere shapes through equal axis scaling

#### Advanced Parameters
- `-i, --interactive`: Enable interactive atomic radius scaling controls
- `-a, --auto-scale`: Automatically calculate optimal scale factor
- `-o, --overlap`: Target overlap ratio for auto-scaling (0.0-1.0)
- `-b, --bonds`: Show chemical bonds between atoms
- `-c, --cutoff`: Bond cutoff distance in Angstroms
- `--scale`: Manual scale factor for atomic radii
- `--no-overlap-info`: Hide overlap analysis information

#### Lattice Parameter Features
- **Automatic Detection**: Reads lattice parameters from `# CELL` line in .hkl files
- **Real Space Conversion**: Converts fractional coordinates to Angstrom coordinates
- **Non-Orthogonal Support**: Handles triclinic, monoclinic, and orthorhombic systems
- **Accurate Distances**: Bond detection and overlap analysis use real space distances
- **Professional Output**: Displays both fractional and real space coordinates

## Enhanced Reciprocal Space Visualization

### Basic Usage

```bash
python3D.py -m reflections filename.hkl
```

This mode provides an advanced 3D visualization of crystal reflections in reciprocal space with comprehensive interactive controls.

### Advanced Features

#### 1. HKL Range Controls
- **H Range Sliders**: Control minimum and maximum H values independently
- **K Range Sliders**: Control minimum and maximum K values independently  
- **L Range Sliders**: Control minimum and maximum L values independently
- **Real-time Filtering**: Updates display immediately as you adjust ranges

#### 2. Intensity and Size Controls
- **Intensity Threshold**: Filter reflections by minimum intensity value
- **Size Factor Slider**: Fine-tune sphere sizes from 1x to 1000x
- **Size Presets**: Quick size adjustments (2x Max, 3x Max, 5x Max)

#### 3. Interactive Control Buttons
- **Show All/Show Filtered**: Toggle between displaying all data or filtered data
- **Reset Ranges**: Reset all range sliders to their full range
- **Reset Size**: Reset the size factor slider to initial value
- **Clear Filter**: Remove all filters and show all data

#### 4. Professional Interface
- **Large Display Area**: 16x14 inch figure for optimal viewing
- **Status Display**: Real-time status showing current filter settings
- **HKL Info Box**: Shows total reflection count and H, K, L ranges on the plot
- **Organized Controls**: All controls positioned below the 3D plot

### Advanced Usage Examples

```bash
# Custom initial size factor
python3 crystal3D.py -m reflections -s 100 filename.hkl

# View specific HKL ranges interactively
python3 crystal3D.py -m reflections filename.hkl
# Then use the sliders to focus on specific regions
```

### Workflow for Analysis

1. **Load Data**: Open your HKL file with the reflections mode
2. **Initial View**: Examine the full dataset to understand the structure
3. **Set Intensity Threshold**: Use the intensity slider to focus on strong reflections
4. **Adjust HKL Ranges**: Use the range sliders to focus on specific regions
5. **Fine-tune Size**: Adjust the size factor for optimal visualization
6. **Toggle Views**: Switch between filtered and unfiltered data as needed
7. **Reset as Needed**: Use reset buttons to return to default settings

## Rotation Schematic Generation

### Basic Usage

```bash
python3 rotation_schematic.py
```

### Features
- **3D Rotation Arrows**: Clear visualization of rotation directions
- **Axis Labels**: Proper labeling of ω (Omega), χ (Chi), and φ (Phi) axes
- **Right-Handed System**: Follows standard crystallographic conventions
- **Professional Appearance**: Publication-ready schematics

### Saving Options

```bash
python3 rotation_schematic.py --save rotation_schematic.png
```

## HKL Reflections Analysis

### Basic Usage

```bash
python3 hkl_reflections.py filename.hkl
```

### Features
- **Interactive 3D Plot**: Navigate through reciprocal space
- **Real-time Filtering**: Adjust H, K, L ranges and intensity thresholds
- **Size Controls**: Customize reflection sphere sizes
- **Professional Interface**: Large display area with organized controls

## File Format Support

### HKL Files
- **Crystal Structure Data**: Atomic coordinates and properties
- **Reflection Data**: H, K, L indices and intensity values
- **Standard Format**: Compatible with crystallographic software

### CIF Files
- **Crystal Information Files**: Standard crystallographic format
- **Structure Data**: Unit cell parameters and atomic coordinates

## Tips for Best Results

### Performance
- **Large Datasets**: Use intensity filtering to focus on important reflections
- **Memory Management**: The enhanced controls efficiently handle large HKL files
- **Real-time Updates**: All controls provide immediate visual feedback

### Visualization Quality
- **Size Factors**: Start with moderate size factors (50-100) for clarity
- **Range Selection**: Use HKL ranges to focus on specific regions of interest
- **Intensity Thresholds**: Set minimum intensity to reduce visual clutter

### Professional Output
- **High Resolution**: Use the large figure size for presentations
- **Color Schemes**: The viridis colormap provides excellent contrast
- **Export Options**: Save high-quality images for publications

## Troubleshooting

### Common Issues
- **No Data Displayed**: Check file format and ensure data is in the expected format
- **Controls Not Responding**: Ensure you're using the correct mode (-m reflections)
- **Performance Issues**: Use intensity filtering for very large datasets

### Getting Help
- Check the troubleshooting guide for specific error messages
- Review the API reference for technical details
- Ensure all dependencies are properly installed

## Advanced Features

### Custom Filtering
- **Combined Filters**: Use multiple range sliders together for precise control
- **Dynamic Updates**: All changes update the display in real-time
- **Filter Persistence**: Filters remain active until manually reset

### Data Analysis
- **Reflection Counting**: Real-time display of visible reflection counts
- **Range Information**: Continuous feedback on current HKL ranges
- **Intensity Analysis**: Focus on strong reflections for structure determination

This enhanced toolset provides professional-grade crystallographic analysis capabilities suitable for research, education, and publication purposes.
