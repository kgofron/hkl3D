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

## Python plots intensities
* ./hkl_reflections.py EntryWithCollCode176.hk
* Dependencies
	* pip install numpy matplotlib
