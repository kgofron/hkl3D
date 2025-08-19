# Troubleshooting

This guide helps you resolve common issues and problems when using HKL3D.

## 🚨 Common Issues

### Display Problems

#### Issue 1: No Display Window Appears

**Symptoms:**
- Script runs without errors
- No matplotlib window opens
- No error messages

**Possible Causes:**
1. **Matplotlib Backend Issues**: Wrong backend configured
2. **Display Environment**: Missing display server
3. **Python Environment**: Virtual environment issues

**Solutions:**

**Solution 1: Set Matplotlib Backend**
```bash
# Linux/macOS
export MPLBACKEND=TkAgg

# Windows
set MPLBACKEND=TkAgg

# Then run your script
python3 hkl_reflections.py your_file.hkl
```

**Solution 2: Check Display Environment**
```bash
# Check if display is available
echo $DISPLAY

# If empty, set it
export DISPLAY=:0

# For remote connections, use X11 forwarding
ssh -X username@remote_host
```

**Solution 3: Install Required Packages**
```bash
# Install Tkinter (Linux)
sudo apt-get install python3-tk

# Install Tkinter (macOS)
brew install python-tk

# Install Tkinter (Windows)
# Usually included with Python installation
```

#### Issue 2: Display is Slow or Unresponsive

**Symptoms:**
- Sliders move slowly
- Plot updates are delayed
- Interface feels sluggish

**Possible Causes:**
1. **Large Dataset**: Too many reflections to display
2. **System Resources**: Insufficient RAM or CPU
3. **Matplotlib Performance**: Backend performance issues

**Solutions:**

**Solution 1: Reduce Data Size**
```bash
# Use more aggressive filtering
python3 hkl_reflections.py your_file.hkl

# In the interface:
# 1. Increase Intensity Min threshold
# 2. Narrow H, K, L ranges
# 3. Use "Show Filtered" mode
```

**Solution 2: Optimize System**
```bash
# Close other applications
# Increase available RAM
# Use SSD storage for better I/O
```

**Solution 3: Change Backend**
```bash
# Try different backends
export MPLBACKEND=Qt5Agg    # Qt backend
export MPLBACKEND=GTK3Agg   # GTK backend
export MPLBACKEND=WXAgg     # WX backend
```

### Lattice Parameter Issues

#### Issue: Lattice parameters not found in .hkl file

**Symptoms:**
- Warning message: "No lattice parameters found in file. Using default values."
- Incorrect coordinate conversion
- Wrong real space distances

**Possible Causes:**
1. **Missing CELL line**: .hkl file doesn't contain `# CELL` information
2. **Wrong file format**: File is not in expected HKL format
3. **Corrupted data**: CELL line is malformed

**Solutions:**

**Solution 1: Check .hkl file format**
```bash
# Look for this line in your .hkl file:
# CELL   18.49400   4.99100  25.83200  90.00000 117.75000  90.00000

# If missing, the file may not be a proper crystallographic HKL file
```

**Solution 2: Verify file structure**
```bash
# Check if file contains crystallographic data
head -20 your_file.hkl

# Should contain:
# - TITLE line
# - CELL line with 6 parameters
# - SPCGRP line
# - Atom data section
```

**Solution 3: Use alternative file**
```bash
# Try with a different .hkl file that has lattice parameters
python3 crystal_structure.py EntryWithCollCode176.hkl
```

#### Issue: Spheres appear as ellipses or distorted

**Symptoms:**
- Atomic spheres look flattened or stretched
- Non-spherical appearance in 3D view
- Inconsistent scaling across axes

**Cause**: Unequal axis scaling in 3D plots

**Solution**: The program now automatically:
- Sets equal aspect ratios (`ax.set_box_aspect([1, 1, 1])`)
- Calculates proper view limits for equal scaling
- Centers the plot to maintain spherical appearance
- Uses higher resolution sphere generation (25 points vs 15)

### File Reading Problems

#### Issue 3: "File Not Found" Error

**Symptoms:**
```
Error: Could not find HKL file filename.hkl
```

**Possible Causes:**
1. **Wrong File Path**: File doesn't exist at specified location
2. **File Permissions**: Insufficient read permissions
3. **Working Directory**: Script running from wrong directory

**Solutions:**

**Solution 1: Check File Path**
```bash
# List files in current directory
ls -la *.hkl

# Check if file exists
ls -la your_file.hkl

# Use absolute path
python3 hkl_reflections.py /full/path/to/your_file.hkl
```

**Solution 2: Fix File Permissions**
```bash
# Check permissions
ls -la your_file.hkl

# Fix permissions if needed
chmod 644 your_file.hkl

# Or make readable by all
chmod a+r your_file.hkl
```

**Solution 3: Check Working Directory**
```bash
# Check current directory
pwd

# Navigate to correct directory
cd /path/to/hkl3d

# Run script
python3 hkl_reflections.py your_file.hkl
```

#### Issue 4: "No Data Found" Error

**Symptoms:**
```
No data found in the file or incorrect format.
```

**Possible Causes:**
1. **Wrong File Format**: File is not a valid HKL file
2. **Corrupted Data**: File structure is damaged
3. **Empty File**: File contains no reflection data

**Solutions:**

**Solution 1: Verify File Format**
```bash
# Check file content
head -20 your_file.hkl

# Look for required headers
grep "H   K   L" your_file.hkl
grep "TITLE" your_file.hkl
```

**Solution 2: Check File Integrity**
```bash
# Check file size
ls -lh your_file.hkl

# Check if file is empty
wc -l your_file.hkl

# Try to read with C++ tool
./read_hkl your_file.hkl
```

**Solution 3: Convert from CIF**
```bash
# If you have a CIF file, convert it
cif2hkl input.cif --output output.hkl

# Then use the HKL file
python3 hkl_reflections.py output.hkl
```

### Data Display Problems

#### Issue 5: No Reflections Visible

**Symptoms:**
- Plot appears empty
- No spheres visible
- Status shows "No reflections match criteria"

**Possible Causes:**
1. **Filter Settings**: Range sliders set too restrictively
2. **Intensity Threshold**: Threshold set too high
3. **Data Range**: H, K, L values outside expected ranges

**Solutions:**

**Solution 1: Reset Filters**
```bash
# In the interface:
# 1. Click "Reset Ranges"
# 2. Click "Reset Size"
# 3. Click "Clear Filter"
# 4. Click "Show All"
```

**Solution 2: Check Data Ranges**
```bash
# Look at the HKL info box on the plot
# Check H, K, L ranges displayed
# Adjust sliders to match these ranges
```

**Solution 3: Lower Intensity Threshold**
```bash
# Move Intensity Min slider to minimum value
# This shows all reflections regardless of intensity
```

#### Issue 6: Overplotting or Multiple Colorbars

**Symptoms:**
- Multiple colorbars stacked
- Visual artifacts
- Poor display quality

**Possible Causes:**
1. **Matplotlib Bug**: Known issue with 3D scatter updates
2. **Multiple Updates**: Rapid slider movements
3. **Memory Issues**: Insufficient cleanup

**Solutions:**

**Solution 1: Restart the Application**
```bash
# Close the matplotlib window
# Restart the script
python3 hkl_reflections.py your_file.hkl
```

**Solution 2: Use Stable Version**
```bash
# Update matplotlib
pip install --upgrade matplotlib

# Or use specific version
pip install matplotlib==3.5.3
```

**Solution 3: Clear Display**
```bash
# In the interface:
# 1. Click "Clear Filter"
# 2. Click "Show All"
# This recreates the display cleanly
```

### C++ Compilation Problems

#### Issue 7: Compilation Errors

**Symptoms:**
```
g++: command not found
error: 'std::string' was not declared
```

**Possible Causes:**
1. **Missing Compiler**: C++ compiler not installed
2. **Wrong Compiler Version**: Incompatible compiler
3. **Missing Libraries**: Standard library not found

**Solutions:**

**Solution 1: Install C++ Compiler**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install build-essential

# CentOS/RHEL
sudo yum groupinstall "Development Tools"

# macOS
xcode-select --install

# Windows
# Install Visual Studio Build Tools
```

**Solution 2: Check Compiler Version**
```bash
# Check GCC version
gcc --version

# Should be 4.9 or higher
# If older, update your system
```

**Solution 3: Use Alternative Build Method**
```bash
# Try the build script
chmod +x build.sh
./build.sh

# Or use make
make clean
make
```

#### Issue 8: Runtime Errors in C++ Program

**Symptoms:**
```
Segmentation fault
Floating point exception
```

**Possible Causes:**
1. **Corrupted Input File**: Invalid HKL file
2. **Memory Issues**: Insufficient system memory
3. **File Format**: Unexpected file structure

**Solutions:**

**Solution 1: Validate Input File**
```bash
# Check file format
head -50 your_file.hkl

# Look for proper structure
# Ensure file is not corrupted
```

**Solution 2: Check File Size**
```bash
# Large files may cause issues
ls -lh your_file.hkl

# If very large (>100MB), consider splitting
```

**Solution 3: Debug with Smaller File**
```bash
# Test with known good file
./read_hkl EntryWithCollCode176.hkl

# If this works, issue is with your file
```

### Performance Issues

#### Issue 9: Slow Loading or Processing

**Symptoms:**
- Long startup time
- Sluggish interface
- High memory usage

**Possible Causes:**
1. **Large Dataset**: Too many reflections
2. **System Resources**: Limited RAM/CPU
3. **File I/O**: Slow storage

**Solutions:**

**Solution 1: Optimize Data Size**
```bash
# Use filtering to reduce visible data
# Start with high intensity threshold
# Narrow H, K, L ranges initially
```

**Solution 2: System Optimization**
```bash
# Close unnecessary applications
# Increase available RAM
# Use faster storage (SSD)
```

**Solution 3: Batch Processing**
```bash
# Process files one at a time
# Don't run multiple instances simultaneously
# Use "Show Filtered" mode for large datasets
```

#### Issue 10: Memory Errors

**Symptoms:**
```
MemoryError: Unable to allocate array
Killed (out of memory)
```

**Possible Causes:**
1. **Insufficient RAM**: System doesn't have enough memory
2. **Large Dataset**: File too large for available memory
3. **Memory Leaks**: Poor memory management

**Solutions:**

**Solution 1: Check System Memory**
```bash
# Check available memory
free -h

# Check memory usage
top
htop
```

**Solution 2: Reduce Data Size**
```bash
# Use aggressive filtering
# Process smaller regions
# Close other applications
```

**Solution 3: Use Virtual Memory**
```bash
# Increase swap space (Linux)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## 🔧 Advanced Troubleshooting

### Debug Mode

Enable verbose output for debugging:

```bash
# Python scripts
python3 -v hkl_reflections.py your_file.hkl

# C++ program
g++ -g -Wall -Wextra -std=c++11 -o read_hkl read_hkl.cpp
./read_hkl your_file.hkl
```

### Log Files

Check for error logs:

```bash
# System logs
dmesg | tail -20

# Application logs
journalctl -u your-service

# Python errors
python3 hkl_reflections.py your_file.hkl 2>&1 | tee error.log
```

### Environment Variables

Set debugging environment variables:

```bash
# Matplotlib debugging
export MPLDEBUG=1

# Python debugging
export PYTHONVERBOSE=1

# C++ debugging
export GDB=1
```

## 🆘 Getting Help

### Before Asking for Help

1. **Check this guide** for your specific issue
2. **Verify your setup** meets requirements
3. **Test with sample data** (EntryWithCollCode176.hkl)
4. **Check system resources** (RAM, CPU, storage)

### Information to Provide

When reporting issues, include:

1. **Operating System**: Linux distribution, macOS version, Windows version
2. **Python Version**: `python3 --version`
3. **Package Versions**: `pip list | grep -E "(numpy|matplotlib)"`
4. **Error Messages**: Complete error output
5. **File Information**: Size, format, source
6. **System Resources**: RAM, CPU, storage

### Support Resources

1. **Project Issues**: GitHub/GitLab issue tracker
2. **Documentation**: Check other docs in this folder
3. **Community**: Crystallography forums and groups
4. **Professional Support**: Contact your institution's IT support

## 🚀 Prevention Tips

### Best Practices

1. **Regular Updates**: Keep Python packages updated
2. **Backup Data**: Keep copies of important HKL files
3. **Test Environment**: Test new features in isolated environment
4. **Monitor Resources**: Watch system resource usage

### System Maintenance

1. **Clean Installation**: Remove old versions before installing new ones
2. **Virtual Environments**: Use virtual environments for Python packages
3. **Regular Updates**: Keep system packages updated
4. **Disk Space**: Maintain adequate free disk space

---

*Last updated: 2025*
