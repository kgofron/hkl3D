# HKL3D Documentation

Welcome to the HKL3D project documentation! This project provides tools for visualizing single crystal diffraction intensities and crystal structures from HKL files.

## 📚 Documentation Index

- **[Installation Guide](installation.md)** - How to set up and install HKL3D
- **[User Guide](user-guide.md)** - How to use the various tools and scripts
- **[API Reference](api-reference.md)** - Detailed documentation of functions and classes
- **[File Formats](file-formats.md)** - Understanding HKL and CIF file formats
- **[Examples](examples.md)** - Practical examples and use cases
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## 🚀 Quick Start

1. **Install dependencies**: `pip install numpy matplotlib`
2. **Run HKL reflections visualization**: `python3 hkl_reflections.py your_file.hkl`
3. **View crystal structure**: `python3 crystal_structure.py your_file.hkl`
4. **Generate rotation schematic**: `python3 rotation_schematic.py`

## 🎯 What is HKL3D?

HKL3D is a collection of Python and C++ tools for analyzing crystallographic data:

- **HKL File Processing**: Read and parse diffraction intensity data
- **3D Visualization**: Interactive 3D plots of crystal reflections
- **Range Controls**: Adjustable H, K, L space filtering
- **Crystal Structure Display**: Visualize atomic positions
- **Diffractometer Schematic**: Rotation axis visualization

## 📁 Project Structure

```
hkl3D/
├── docs/                    # This documentation
├── hkl_reflections.py      # Main HKL visualization tool
├── crystal_structure.py    # Crystal structure viewer
├── crystal3D.py           # Combined functionality
├── rotation_schematic.py   # Diffractometer rotation diagram
├── read_hkl.cpp           # C++ HKL file reader
├── *.hkl                  # Sample HKL data files
└── README.md              # Project overview
```

## 🔬 Scientific Background

This project is designed for crystallographers and materials scientists working with:
- Single crystal diffraction data
- Neutron scattering experiments
- X-ray crystallography
- Crystal structure analysis

## 📖 Getting Help

- Check the [Troubleshooting](troubleshooting.md) guide for common issues
- Review [Examples](examples.md) for usage patterns
- Consult the [API Reference](api-reference.md) for technical details

## 🤝 Contributing

Contributions are welcome! Please see the main project README for contribution guidelines.

---

*Last updated: 2025*
