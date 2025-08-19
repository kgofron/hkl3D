# Examples

*Last updated: 2025*

This document provides practical examples and use cases for the HKL3D project tools.

## Crystal Structure Visualization

### Basic Atomic Structure Display

View the atomic structure of a crystal from an HKL file:

```bash
python3 crystal3D.py -m atoms EntryWithCollCode176.hkl
```

**What you'll see:**
- 3D scatter plot with Si atoms (red squares) and O atoms (blue circles)
- Interactive 3D navigation (rotate, zoom, pan)
- Equal aspect ratio maintaining crystallographic proportions
- Professional layout suitable for publications

### Custom Analysis Script

Create a custom script to analyze specific atomic positions:

```python
from crystal3D import read_crystal_structure

# Load crystal structure
atoms = read_crystal_structure('EntryWithCollCode176.hkl')

# Find Si atoms in specific region
si_atoms = [atom for atom in atoms if atom['name'].startswith('Si')]
central_si = [atom for atom in si_atoms if abs(atom['x']) < 0.1 and 
                                             abs(atom['y']) < 0.1 and 
                                             abs(atom['z']) < 0.1]

print(f"Found {len(central_si)} Si atoms in central region:")
for atom in central_si:
    print(f"  {atom['name']}: ({atom['x']:.3f}, {atom['y']:.3f}, {atom['z']:.3f})")
```

## Enhanced Reciprocal Space Visualization

### Basic Reflection Display

View crystal reflections with all enhanced controls:

```bash
python3 crystal3D.py -m reflections EntryWithCollCode55782.hkl
```

**Enhanced Features Available:**
- **HKL Range Controls**: Independent H, K, L min/max sliders
- **Intensity Filtering**: Focus on strong reflections
- **Size Controls**: Fine-tune sphere sizes from 1x to 1000x
- **Interactive Buttons**: Toggle views, reset settings, clear filters
- **Professional Interface**: Large 16x14 inch display with organized controls

### Custom Size Factor

Start with a larger size factor for better visibility:

```bash
python3 crystal3D.py -m reflections -s 100 EntryWithCollCode55782.hkl
```

### Advanced Filtering Workflow

1. **Load Data**: Open the reflections mode
2. **Initial Assessment**: View the complete dataset to understand the structure
3. **Set Intensity Threshold**: Use the intensity slider to focus on strong reflections
4. **Focus on Specific Region**: Adjust H, K, L ranges to focus on areas of interest
5. **Fine-tune Size**: Use the size factor slider for optimal visibility
6. **Toggle Views**: Switch between filtered and complete datasets as needed

### Custom Analysis with Enhanced Controls

```python
from crystal3D import read_hkl_reflections, plot_reflections

# Load reflection data
reflections = read_hkl_reflections('EntryWithCollCode55782.hkl')

# Pre-filter for strong reflections
strong_reflections = [r for r in reflections if r[3] > 0.5]

# Visualize with enhanced controls
plot_reflections(strong_reflections, initial_size=75)

# The enhanced interface will provide:
# - HKL range sliders for further filtering
# - Intensity threshold adjustment
# - Size factor controls
# - Interactive buttons for view management
```

## Rotation Schematic Generation

### Basic Schematic

Generate a standard diffractometer rotation diagram:

```bash
python3 rotation_schematic.py
```

**Features Displayed:**
- ω (Omega): X-axis rotation (red arrows)
- χ (Chi): Y-axis rotation (green arrows)
- φ (Phi): Z-axis rotation (blue arrows)
- Right-handed coordinate system
- Clear rotation direction indicators

### Save for Publication

Save the schematic as a high-resolution image:

```bash
python3 rotation_schematic.py --save rotation_schematic.png
```

### Custom Schematic Script

```python
from rotation_schematic import create_rotation_arrows, plot_rotation_schematic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create custom schematic
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Add custom rotation arrows
create_rotation_arrows(ax, [0, 0, 0], radius=1.5, axis='z', color='purple', alpha=0.8)

# Customize the display
ax.set_title('Custom Rotation Schematic')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

plt.show()
```

## HKL Reflections Analysis (Legacy)

### Basic Usage

Use the standalone HKL reflections tool:

```bash
python3 hkl_reflections.py EntryWithCollCode55782.hkl
```

**Note**: This tool now has the same enhanced features as `crystal3D.py -m reflections`

## Advanced Workflows

### Structure Determination Analysis

1. **Load Crystal Structure**: Understand the atomic arrangement
   ```bash
   python3 crystal3D.py -m atoms structure.hkl
   ```

2. **Analyze Reflections**: Examine the reciprocal space data
   ```bash
   python3 crystal3D.py -m reflections structure.hkl
   ```

3. **Focus on Strong Reflections**: Use intensity filtering to identify key reflections
4. **Examine Specific Regions**: Use HKL range controls to focus on particular areas
5. **Document Findings**: Save views and export data for publication

### Batch Processing

Process multiple HKL files automatically:

```bash
#!/bin/bash
# Process all HKL files in current directory
for file in *.hkl; do
    echo "Processing $file..."
    
    # Generate reflection visualization
    python3 crystal3D.py -m reflections "$file" &
    
    # Wait a bit between files
    sleep 2
done
```

### Custom Filtering Script

```python
import os
from crystal3D import read_hkl_reflections

def analyze_reflections(filename, h_range=(-5, 5), k_range=(-5, 5), l_range=(-5, 5), min_intensity=0.1):
    """Analyze reflections with custom filtering criteria."""
    
    # Load data
    reflections = read_hkl_reflections(filename)
    
    # Apply filters
    filtered = []
    for h, k, l, intensity in reflections:
        if (h_range[0] <= h <= h_range[1] and 
            k_range[0] <= k <= k_range[1] and 
            l_range[0] <= l <= l_range[1] and 
            intensity >= min_intensity):
            filtered.append((h, k, l, intensity))
    
    print(f"File: {filename}")
    print(f"Total reflections: {len(reflections)}")
    print(f"Filtered reflections: {len(filtered)}")
    print(f"Strongest reflection: {max(filtered, key=lambda x: x[3])}")
    print()
    
    return filtered

# Analyze multiple files
files = ['file1.hkl', 'file2.hkl', 'file3.hkl']
for file in files:
    if os.path.exists(file):
        analyze_reflections(file, h_range=(-3, 3), min_intensity=0.5)
```

## Interactive Crystal Structure Examples

### Basic Interactive Mode

```bash
# Enable interactive atomic radius scaling (unified tool)
python3 crystal3D.py EntryWithCollCode176.hkl -m atoms -i

# Interactive mode with auto-scaling
python3 crystal3D.py EntryWithCollCode176.hkl -m atoms -a -i

# Interactive mode with bonds
python3 crystal3D.py EntryWithCollCode176.hkl -m atoms -b -i

# Full interactive experience
python3 crystal3D.py EntryWithCollCode176.hkl -m atoms -a -b -i

# Legacy tool (still available)
python3 crystal_structure.py EntryWithCollCode176.hkl -i
```

## Unified Crystal3D Tool Examples

### Enhanced Crystal Structure Mode

```bash
# Basic enhanced visualization with lattice parameters
python3 crystal3D.py data.hkl -m atoms

# Interactive atomic radius scaling
python3 crystal3D.py data.hkl -m atoms -i

# Auto-scaling for optimal visibility
python3 crystal3D.py data.hkl -m atoms -a

# Interactive mode with auto-scaling
python3 crystal3D.py data.hkl -m atoms -a -i

# Show chemical bonds with interactive controls
python3 crystal3D.py data.hkl -m atoms -b -i

# Full enhanced experience
python3 crystal3D.py data.hkl -m atoms -a -b -i
```

### Legacy Tool with Lattice Parameters

```bash
# Enhanced crystal structure with automatic lattice parameter reading
python3 crystal_structure.py data.hkl

# Auto-scaling using real space coordinates
python3 crystal_structure.py data.hkl -a

# Interactive mode with lattice-aware scaling
python3 crystal_structure.py data.hkl -a -i

# Show bonds using real space distances
python3 crystal_structure.py data.hkl -b -i
```

### Enhanced Reflections Mode

```bash
# Basic reflection visualization
python3 crystal3D.py data.hkl -m reflections

# Custom size factor
python3 crystal3D.py data.hkl -m reflections -s 100

# Large size for visibility
python3 crystal3D.py data.hkl -m reflections -s 500
```

### Lattice Parameter Examples

#### Automatic Lattice Parameter Reading
```bash
# The program automatically reads lattice parameters from .hkl files
python3 crystal_structure.py EntryWithCollCode176.hkl

# Output shows:
# Lattice parameters: a=18.494, b=4.991, c=25.832
# Angles: α=90.00°, β=117.75°, γ=90.00°
```

#### Real Space Coordinate Conversion
```bash
# Atoms are plotted in real space coordinates (Å) instead of fractional
python3 crystal_structure.py data.hkl -a

# The analysis shows both coordinate systems:
# Fractional: (0.020000, 0.189600, 0.038000)
# Real Space: (-0.09, 0.95, 0.87) Å
```

### Interactive Workflow Examples

#### Research Analysis Workflow
```bash
# Step 1: Start with auto-scaling for optimal initial view
python3 crystal3D.py data.hkl -m atoms -a -i

# Use the interface:
# 1. Observe the auto-calculated scale factor
# 2. Use the slider to fine-tune the visualization
# 3. Click "Optimal" for no-overlap scaling
# 4. Use "Reset" to return to 1.0x scaling
# 5. Monitor the Status box for real-time feedback
```

#### Educational Demonstration Workflow
```bash
# Step 1: Start with default scaling and bonds
python3 crystal_structure.py data.hkl -b -i

# Interactive demonstration:
# 1. Show students the realistic atomic sizes (1.0x scale)
# 2. Use slider to reduce scale for better visibility
# 3. Explain chemical bonding with bond visualization
# 4. Use "Auto-Scale" to show optimal scientific scaling
```

#### Publication Preparation Workflow
```bash
# Step 1: Start with comprehensive analysis
python3 crystal_structure.py data.hkl -a -b -i

# Publication workflow:
# 1. Use auto-scaling for scientifically accurate proportions
# 2. Fine-tune with slider for optimal visibility
# 3. Enable bonds for complete structural information
# 4. Use Status box to document exact scale factor used
# 5. Take screenshots at optimal scaling for publication
```

### Interactive Controls Reference

#### Scale Slider
- **Range**: 0.01x to 1.0x atomic radii
- **Use**: Primary control for real-time scaling adjustment
- **Tip**: Start with auto-scaling, then fine-tune with slider

#### Control Buttons
- **Reset**: Return to 1.0x scaling (realistic atomic sizes)
- **Auto-Scale**: Apply calculated optimal scaling for visibility
- **Optimal**: Calculate no-overlap scaling for maximum clarity

#### Information Display
- **Scale Factor Box**: Shows current scaling and distance information
- **Status Box**: Provides real-time feedback on operations
- **Legend**: Updates automatically with scaled atomic radii

## Integration Examples

### Custom Analysis Dashboard

```python
import matplotlib.pyplot as plt
from crystal3D import read_hkl_reflections, read_crystal_structure
import numpy as np

def create_analysis_dashboard(hkl_file):
    """Create a comprehensive analysis dashboard."""
    
    # Load data
    reflections = read_hkl_reflections(hkl_file)
    atoms = read_crystal_structure(hkl_file)
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: HKL distribution
    h, k, l, intensities = zip(*reflections)
    ax1.scatter(h, k, c=intensities, cmap='viridis', alpha=0.6)
    ax1.set_xlabel('H')
    ax1.set_ylabel('K')
    ax1.set_title('H-K Distribution')
    
    # Plot 2: Intensity histogram
    ax2.hist(intensities, bins=50, alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Intensity')
    ax2.set_ylabel('Count')
    ax2.set_title('Intensity Distribution')
    
    # Plot 3: L vs Intensity
    ax3.scatter(l, intensities, alpha=0.6)
    ax3.set_xlabel('L')
    ax3.set_ylabel('Intensity')
    ax3.set_title('L vs Intensity')
    
    # Plot 4: Atom positions (top view)
    si_atoms = [atom for atom in atoms if atom['name'].startswith('Si')]
    o_atoms = [atom for atom in atoms if atom['name'].startswith('O')]
    
    si_x, si_y = zip(*[(atom['x'], atom['y']) for atom in si_atoms])
    o_x, o_y = zip(*[(atom['x'], atom['y']) for atom in o_atoms])
    
    ax4.scatter(si_x, si_y, c='red', marker='s', s=100, label='Si')
    ax4.scatter(o_x, o_y, c='blue', marker='o', s=80, label='O')
    ax4.set_xlabel('X (fractional)')
    ax4.set_ylabel('Y (fractional)')
    ax4.set_title('Atomic Positions (Top View)')
    ax4.legend()
    
    plt.tight_layout()
    plt.show()

# Use the dashboard
create_analysis_dashboard('EntryWithCollCode55782.hkl')
```

### Export and Reporting

```python
def export_analysis_report(hkl_file, output_file):
    """Export analysis results to a text report."""
    
    reflections = read_hkl_reflections(hkl_file)
    atoms = read_crystal_structure(hkl_file)
    
    with open(output_file, 'w') as f:
        f.write(f"HKL Analysis Report: {hkl_file}\n")
        f.write("=" * 50 + "\n\n")
        
        # Summary statistics
        f.write(f"Total reflections: {len(reflections)}\n")
        f.write(f"Total atoms: {len(atoms)}\n\n")
        
        # Intensity analysis
        intensities = [r[3] for r in reflections]
        f.write(f"Intensity statistics:\n")
        f.write(f"  Minimum: {min(intensities):.2e}\n")
        f.write(f"  Maximum: {max(intensities):.2e}\n")
        f.write(f"  Mean: {np.mean(intensities):.2e}\n")
        f.write(f"  Median: {np.median(intensities):.2e}\n\n")
        
        # Strongest reflections
        f.write("Top 10 strongest reflections:\n")
        sorted_reflections = sorted(reflections, key=lambda x: x[3], reverse=True)
        for i, (h, k, l, intensity) in enumerate(sorted_reflections[:10]):
            f.write(f"  {i+1:2d}. HKL({h:3d},{k:3d},{l:3d}): {intensity:.2e}\n")
        
        f.write("\nReport generated successfully!\n")
    
    print(f"Analysis report saved to {output_file}")

# Generate report
export_analysis_report('EntryWithCollCode55782.hkl', 'analysis_report.txt')
```

## Best Practices

### Performance Optimization

1. **Use Intensity Filtering**: Start with intensity thresholds to reduce data size
2. **Gradual Range Adjustment**: Make small changes to HKL ranges for smooth updates
3. **Size Factor Management**: Use moderate size factors (50-200) for best performance
4. **Memory Management**: Close plots when not needed to free memory

### Visualization Quality

1. **Start with Full Range**: Begin with complete dataset to understand structure
2. **Focus on Strong Reflections**: Use intensity filtering to identify key features
3. **Use Appropriate Size Factors**: Balance visibility with performance
4. **Save Important Views**: Export high-quality images for documentation

### Data Analysis

1. **Systematic Filtering**: Use HKL ranges methodically to explore different regions
2. **Document Settings**: Note filter settings for reproducible results
3. **Compare Views**: Use toggle functionality to compare filtered vs. complete data
4. **Export Results**: Save filtered datasets for further analysis

These examples demonstrate the comprehensive capabilities of the enhanced HKL3D tools, providing professional-grade crystallographic analysis suitable for research, education, and publication purposes.
