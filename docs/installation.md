# Installation Guide

This guide will help you install and set up HKL3D on your system.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows
- **Python**: Version 3.7 or higher
- **C++ Compiler**: GCC 4.9+ (Linux/macOS) or Visual Studio (Windows)

### Python Dependencies
The following Python packages are required:
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization

## 🚀 Installation Methods

### Method 1: Using pip (Recommended)

1. **Install Python dependencies**:
   ```bash
   pip install numpy matplotlib
   ```

2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd hkl3D
   ```

3. **Verify installation**:
   ```bash
   python3 -c "import numpy, matplotlib; print('Dependencies installed successfully!')"
   ```

### Method 2: Using conda

1. **Create a new conda environment**:
   ```bash
   conda create -n hkl3d python=3.9
   conda activate hkl3d
   ```

2. **Install dependencies**:
   ```bash
   conda install numpy matplotlib
   ```

3. **Clone and navigate to the project**:
   ```bash
   git clone <repository-url>
   cd hkl3D
   ```

### Method 3: Manual Installation

1. **Install Python packages manually**:
   ```bash
   # Download and install numpy
   pip install numpy
   
   # Download and install matplotlib
   pip install matplotlib
   ```

2. **Verify matplotlib backend**:
   ```bash
   python3 -c "import matplotlib; print('Backend:', matplotlib.get_backend())"
   ```

## 🔧 Building C++ Components

### Linux/macOS

1. **Using make**:
   ```bash
   make
   ```

2. **Using the build script**:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

3. **Manual compilation**:
   ```bash
   g++ -Wall -Wextra -std=c++11 -o read_hkl read_hkl.cpp
   ```

### Windows

1. **Using Visual Studio**:
   - Open `read_hkl.cpp` in Visual Studio
   - Build the project (Ctrl+Shift+B)

2. **Using MinGW**:
   ```cmd
   g++ -Wall -Wextra -std=c++11 -o read_hkl.exe read_hkl.cpp
   ```

## ✅ Verification

### Test Python Installation

```bash
# Test basic functionality
python3 -c "
import numpy as np
import matplotlib.pyplot as plt
print('NumPy version:', np.__version__)
print('Matplotlib version:', plt.matplotlib.__version__)
print('Installation successful!')
"
```

### Test C++ Compilation

```bash
# Test the C++ program
./read_hkl EntryWithCollCode176.hkl
```

### Test Python Scripts

```bash
# Test HKL reflections visualization
python3 hkl_reflections.py EntryWithCollCode176.hkl

# Test crystal structure viewer
python3 crystal_structure.py EntryWithCollCode176.hkl

# Test rotation schematic
python3 rotation_schematic.py
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Matplotlib Backend Issues
**Problem**: No display window appears
**Solution**: 
```bash
# Set matplotlib backend
export MPLBACKEND=TkAgg  # Linux/macOS
# or
set MPLBACKEND=TkAgg     # Windows
```

#### 2. Missing Dependencies
**Problem**: Import errors
**Solution**: Install missing packages
```bash
pip install --upgrade numpy matplotlib
```

#### 3. C++ Compilation Errors
**Problem**: Compiler not found or compilation fails
**Solution**: Install development tools
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# CentOS/RHEL
sudo yum groupinstall "Development Tools"

# macOS
xcode-select --install
```

#### 4. Permission Issues
**Problem**: Cannot execute build scripts
**Solution**: Make scripts executable
```bash
chmod +x build.sh
chmod +x *.py
```

## 🔍 Environment Variables

You may need to set these environment variables:

```bash
# For matplotlib display
export MPLBACKEND=TkAgg

# For Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/hkl3D"

# For C++ compilation
export CXX=g++
export CC=gcc
```

## 📱 Platform-Specific Notes

### Linux
- Most distributions include Python 3 and development tools
- Use package manager for system-wide installations
- Consider using virtual environments for Python packages

### macOS
- Install Xcode Command Line Tools for C++ compilation
- Use Homebrew for additional dependencies if needed
- Python 3 is usually pre-installed

### Windows
- Install Visual Studio Build Tools for C++ compilation
- Use Anaconda/Miniconda for Python environment management
- Consider WSL for Linux-like development experience

## 🆘 Getting Help

If you encounter installation issues:

1. Check the [Troubleshooting](troubleshooting.md) guide
2. Verify your system meets the prerequisites
3. Check the error messages for specific dependency issues
4. Ensure you have the correct Python version

---

*Last updated: 2025*
