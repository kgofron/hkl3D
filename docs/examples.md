# Examples

This document provides practical examples and use cases for HKL3D, demonstrating how to use the various tools and features.

## 🚀 Getting Started Examples

### Basic HKL Visualization

#### Example 1: View HKL Reflections
```bash
# Basic usage with default settings
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**What happens:**
- Loads all HKL reflections from the file
- Displays 3D scatter plot with default size factor (50)
- Shows interactive controls for range filtering

#### Example 2: Custom Size Factor
```bash
# Start with larger spheres for better visibility
python3 hkl_reflections.py -s 100 EntryWithCollCode176.hkl
```

**Result:**
- Initial sphere size is 2x larger than default
- Better visibility for presentations
- Easier to see reflection patterns

#### Example 3: Different Crystal System
```bash
# View tetragonal crystal data
python3 hkl_reflections.py ErRu2Si2/EntryWithCollCode55782.hkl
```

**Features:**
- Different H, K, L ranges (tetragonal vs monoclinic)
- Different intensity distributions
- Different reflection patterns

## 🔍 Interactive Analysis Examples

### Range Filtering Workflows

#### Example 4: Focus on Specific H Values
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Workflow:**
1. **Load data** - All reflections visible
2. **Adjust H Range** - Set H Min to 0, H Max to 2
3. **Click "Show Filtered"** - Only reflections with H=0,1,2 visible
4. **Observe pattern** - Notice clustering in H direction

#### Example 5: Intensity-Based Filtering
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Workflow:**
1. **Load data** - All reflections visible
2. **Adjust Intensity Min** - Increase to show only strong reflections
3. **Click "Show Filtered"** - Only high-intensity reflections visible
4. **Analyze** - Strong reflections often indicate important structural features

#### Example 6: Combined Filtering
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Workflow:**
1. **Set H Range** - H Min: -2, H Max: 2
2. **Set K Range** - K Min: -1, K Max: 1  
3. **Set L Range** - L Min: 0, L Max: 4
4. **Set Intensity Min** - High threshold for strong reflections
5. **Click "Show Filtered"** - Focused view of specific region

### Size Adjustment Examples

#### Example 7: Size Presets
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Workflow:**
1. **Load data** - Default size factor
2. **Click "2x Max"** - Double sphere sizes
3. **Click "3x Max"** - Triple sphere sizes
4. **Click "5x Max"** - Five times sphere sizes
5. **Use Size Factor slider** - Fine-tune between presets

#### Example 8: Dynamic Size Adjustment
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Workflow:**
1. **Load data** - Default settings
2. **Drag Size Factor slider** - Watch spheres grow/shrink in real-time
3. **Find optimal size** - Balance between visibility and clarity
4. **Use Reset Size** - Return to default if needed

## 🏗️ Crystal Structure Examples

### Atomic Position Visualization

#### Example 9: View Silicon Dioxide Structure
```bash
python3 crystal_structure.py EntryWithCollCode176.hkl
```

**What you see:**
- Silicon atoms (Si) in 3D space
- Oxygen atoms (O) surrounding silicon
- Unit cell boundaries
- Atomic coordination patterns

#### Example 10: View ErRu2Si2 Structure
```bash
python3 crystal_structure.py ErRu2Si2/EntryWithCollCode55782.hkl
```

**Features:**
- Erbium atoms at corners
- Ruthenium atoms at face centers
- Silicon atoms in tetrahedral coordination
- Tetragonal symmetry visible

## 🎪 Rotation Schematic Examples

### Diffractometer Visualization

#### Example 11: Basic Rotation Diagram
```bash
python3 rotation_schematic.py
```

**Output:**
- 3D diagram showing rotation axes
- Color-coded coordinate system
- Rotation direction arrows
- Professional presentation layout

#### Example 12: Save High-Resolution Image
```bash
python3 rotation_schematic.py --save rotation_diagram.png
```

**Result:**
- High-resolution PNG file (300 DPI)
- Suitable for publications
- Professional appearance
- Vector-like quality

## 🔧 Combined Tool Examples

### Crystal3D Multi-Mode Usage

#### Example 13: Switch Between Modes
```bash
# Start with reflections view
python3 crystal3D.py -m reflections EntryWithCollCode176.hkl

# Switch to atomic view
python3 crystal3D.py -m atoms EntryWithCollCode176.hkl
```

#### Example 14: Custom Size with Combined Tool
```bash
# Large spheres for presentation
python3 crystal3D.py -m reflections -s 200 EntryWithCollCode176.hkl
```

## 💻 C++ Tool Examples

### Command-Line Data Processing

#### Example 15: Basic HKL Reading
```bash
./read_hkl EntryWithCollCode176.hkl
```

**Output:**
```
Found 178 reflections:
H: 0 K: 0 L: 2 Mult: 1 d-spacing: 11.43050 |Fc|^2: 0.69358575E+00
H: 2 K: 0 L: -2 Mult: 1 d-spacing: 8.89791 |Fc|^2: 0.74799341E+00
...
```

#### Example 16: Process Multiple Files
```bash
# Process all HKL files in directory
for file in *.hkl; do
    echo "Processing $file..."
    ./read_hkl "$file"
    echo "---"
done
```

## 📊 Data Analysis Examples

### Statistical Analysis

#### Example 17: Reflection Statistics
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Information displayed:**
- Total reflection count
- H, K, L ranges
- Intensity distribution
- Data quality metrics

#### Example 18: Crystal System Analysis
```bash
# Compare different crystal systems
python3 hkl_reflections.py EntryWithCollCode176.hkl      # Monoclinic
python3 hkl_reflections.py ErRu2Si2/EntryWithCollCode55782.hkl  # Tetragonal
```

**Observations:**
- Different H, K, L patterns
- Different symmetry constraints
- Different reflection distributions

## 🎨 Visualization Examples

### Presentation-Quality Output

#### Example 19: High-Resolution Screenshots
```bash
# Use matplotlib save functionality
# In the interactive window, use File > Save As
# Or use keyboard shortcut Ctrl+S
```

**Recommended settings:**
- DPI: 300 or higher
- Format: PNG or PDF
- Size: 16x14 inches for HKL plots

#### Example 20: Custom Color Schemes
```bash
# Modify the script to change colormap
# Change 'viridis' to 'plasma', 'inferno', 'magma', etc.
```

## 🚀 Advanced Workflows

### Research Analysis Pipeline

#### Example 21: Complete Analysis Workflow
```bash
# 1. Convert CIF to HKL (if needed)
cif2hkl input.cif --output data.hkl

# 2. Quick data inspection
./read_hkl data.hkl

# 3. Interactive visualization
python3 hkl_reflections.py data.hkl

# 4. Generate rotation schematic
python3 rotation_schematic.py --save schematic.png

# 5. Export filtered data
# Use the interactive controls to select region of interest
```

#### Example 22: Batch Processing
```bash
#!/bin/bash
# Process multiple crystal structures

for crystal in crystals/*.hkl; do
    name=$(basename "$crystal" .hkl)
    echo "Processing $name..."
    
    # Generate visualization
    python3 hkl_reflections.py "$crystal" &
    
    # Wait for user interaction
    read -p "Press Enter when done with $name..."
    
    # Kill the process
    pkill -f "hkl_reflections.py"
done
```

### Integration Examples

#### Example 23: With External Crystallographic Software
```bash
# Use HKL3D for visualization
python3 hkl_reflections.py data.hkl

# Export selected region to other software
# Copy H, K, L values from status display
# Paste into Excel, Python, or other analysis tools
```

#### Example 24: Data Pipeline Integration
```bash
# Automated processing script
python3 -c "
import hkl_reflections
data = hkl_reflections.read_hkl_file('data.hkl')
print(f'Loaded {len(data)} reflections')
print(f'H range: {min(x[0] for x in data)} to {max(x[0] for x in data)}')
print(f'K range: {min(x[1] for x in data)} to {max(x[1] for x in data)}')
print(f'L range: {min(x[2] for x in data)} to {max(x[2] for x in data)}')
"
```

## 🎯 Educational Examples

### Learning Crystallography

#### Example 25: Understanding Miller Indices
```bash
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

**Learning points:**
1. **H=0 reflections**: Show planes parallel to a-axis
2. **K=0 reflections**: Show planes parallel to b-axis  
3. **L=0 reflections**: Show planes parallel to c-axis
4. **Combined indices**: Show inclined planes

#### Example 26: Crystal Symmetry
```bash
# Compare different crystal systems
python3 hkl_reflections.py EntryWithCollCode176.hkl      # Monoclinic
python3 hkl_reflections.py ErRu2Si2/EntryWithCollCode55782.hkl  # Tetragonal
```

**Symmetry observations:**
- **Monoclinic**: Different a, b, c lengths, β ≠ 90°
- **Tetragonal**: a = b ≠ c, all angles = 90°

## 🐛 Troubleshooting Examples

### Common Issues and Solutions

#### Example 27: Fix Display Issues
```bash
# Set matplotlib backend
export MPLBACKEND=TkAgg

# Run visualization
python3 hkl_reflections.py EntryWithCollCode176.hkl
```

#### Example 28: Handle Large Files
```bash
# Use aggressive filtering for large datasets
python3 hkl_reflections.py large_file.hkl

# Set high intensity threshold
# Use narrow H, K, L ranges
# Focus on specific regions
```

## 📚 Further Examples

### Custom Modifications

#### Example 29: Add Custom Analysis
```python
# Modify hkl_reflections.py to add custom features
import numpy as np

def analyze_reflections(hkl_data):
    """Custom analysis function"""
    h_vals = [x[0] for x in hkl_data]
    k_vals = [x[1] for x in hkl_data]
    l_vals = [x[2] for x in hkl_data]
    
    # Calculate statistics
    print(f"H variance: {np.var(h_vals):.2f}")
    print(f"K variance: {np.var(k_vals):.2f}")
    print(f"L variance: {np.var(l_vals):.2f}")
    
    return h_vals, k_vals, l_vals
```

#### Example 30: Export Functions
```python
# Add export functionality
def export_filtered_data(hkl_data, h_range, k_range, l_range, intensity_min):
    """Export filtered data to file"""
    filtered = []
    for h, k, l, intensity in hkl_data:
        if (h_range[0] <= h <= h_range[1] and 
            k_range[0] <= k <= k_range[1] and
            l_range[0] <= l <= l_range[1] and
            intensity >= intensity_min):
            filtered.append((h, k, l, intensity))
    
    with open('filtered_data.txt', 'w') as f:
        f.write("H\tK\tL\tIntensity\n")
        for h, k, l, intensity in filtered:
            f.write(f"{h}\t{k}\t{l}\t{intensity}\n")
    
    return len(filtered)
```

---

*Last updated: 2025*
