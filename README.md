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
* ./hkl_reflections.py EntryWithCollCode176.hk
* Plot real space crystal structure
	* ./crystal_structure.py
* Dependencies
	* pip install numpy matplotlib

* Combined function
	* ./crystal3d.py -m reflections EntryWithCollCode176.hkl
	* ./crystal3d.py -m atoms EntryWithCollCode176.hkl