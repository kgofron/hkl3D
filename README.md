# hkl3D

Plotting single crystal diffraction intensities.
The spec-like .hkl diffraciton intensities are obtained from .cif Crystallographic Information File using
* https://gitlab.com/soleil-data-treatment/soleil-software-projects/cif2hkl

## C++ program is not complete

* You can now build the program in three ways:
	* Using make: make
	* Using the bash script: ./build.sh
	* Using g++ directly: g++ -Wall -Wextra -std=c++11 -o read_hkl read_hkl.cpp
* Run
	* ./read_hkl EntryWithCollCode176.hkl 

## Python plot hkl intensities

#### Reciprocal space

Added radjustment of hkl space size, minimum intensity, size factor (reflection intensity)

* python3 hkl_reflections.py ErRu2Si2/EntryWithCollCode55782.hkl
* ./hkl_reflections.py EntryWithCollCode176.hkl

#### Real space

* Plot real space crystal structure
	* ./crystal_structure.py
* Dependencies
	* pip install numpy matplotlib

* Combined function
	* ./crystal3d.py -m reflections EntryWithCollCode176.hkl
	* ./crystal3d.py -m atoms EntryWithCollCode176.hkl

## 📚 Documentation

Comprehensive documentation is available in the `docs/` folder:

* **[Installation Guide](docs/installation.md)** - Setup and installation instructions
* **[User Guide](docs/user-guide.md)** - How to use all tools and features
* **[API Reference](docs/api-reference.md)** - Technical documentation
* **[File Formats](docs/file-formats.md)** - HKL and CIF format specifications
* **[Examples](docs/examples.md)** - Practical usage examples
* **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions