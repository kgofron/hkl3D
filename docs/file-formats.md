# File Formats

This document describes the file formats supported by HKL3D and their structure.

## 📁 HKL Files

HKL files are the primary format for crystallographic reflection data in HKL3D.

### File Extension
- **Extension**: `.hkl`
- **Format**: Text-based, human-readable
- **Encoding**: ASCII/UTF-8

### File Structure

HKL files consist of several sections:

#### 1. Header Section
```
# TITLE  Crystal description and composition
#        a         b         c       alpha     beta      gamma
# CELL   18.49400   4.99100  25.83200  90.00000 117.75000  90.00000
# SPCGRP  C 1 c 1 [Number    9]
```

**Fields:**
- **TITLE**: Crystal description and chemical formula
- **CELL**: Unit cell parameters (a, b, c in Angstroms, angles in degrees)
- **SPCGRP**: Space group information

#### 2. Atomic Positions Section
```
#                    X         Y         Z         B         Occ       Spin      Charge
# Atom  Si1                    0.02000   0.18960   0.03800   0.00000   1.00000   0.00000   0.00000
# Atom  Si2                    0.20670   0.28990   0.09691   0.00000   1.00000   0.00000   0.00000
```

**Fields:**
- **Atom**: Atom identifier (e.g., Si1, O1)
- **X, Y, Z**: Fractional coordinates in unit cell
- **B**: B-factor (thermal parameter)
- **Occ**: Occupancy (usually 1.0 for fully occupied sites)
- **Spin**: Spin state (for magnetic structures)
- **Charge**: Formal charge

#### 3. Physical Parameters Section
```
# Physical parameters:
# sigma_coh       510.07715 coherent   scattering cross section in [barn]
# sigma_inc         0.26880 incoherent scattering cross section in [barn]
# sigma_abs         8.22624 absorption scattering cross section in [barn]
# density           2.26954 in [g/cm^3]
# weight         2884.04541 in [g/mol]
# Vc             2110.15161 volume of unit cell in [A^3]
```

**Fields:**
- **sigma_coh**: Coherent scattering cross section
- **sigma_inc**: Incoherent scattering cross section
- **sigma_abs**: Absorption cross section
- **density**: Material density
- **weight**: Molecular weight
- **Vc**: Unit cell volume

#### 4. Reflection Data Section
```
# H   K   L     Mult    dspc                   |Fc|^2
   0    0    2     1      11.43050      0.69358575E+00
   2    0   -2     1       8.89791      0.74799341E+00
   2    0    0     1       8.18348      0.38960101E-01
```

**Fields:**
- **H, K, L**: Miller indices (integer values)
- **Mult**: Multiplicity (integer)
- **dspc**: d-spacing in Angstroms (float)
- **|Fc|^2**: Structure factor squared (float)

### Data Types

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| H, K, L | int | Any integer | Miller indices |
| Mult | int | 1+ | Reflection multiplicity |
| dspc | float | > 0 | d-spacing in Å |
| |Fc|² | float | ≥ 0 | Intensity |

### Example HKL File

```hkl
# TITLE  Si4 Si4 Si4 Si4 Si4 Si4 Si4 Si4 Si4 Si4 Si4 Si4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 O4 [Monoclinic, Acentric]
#        a         b         c       alpha     beta      gamma
# CELL   18.49400   4.99100  25.83200  90.00000 117.75000  90.00000
# SPCGRP  C 1 c 1 [Number    9]
#                    X         Y         Z         B         Occ       Spin      Charge
# Atom  Si1                    0.02000   0.18960   0.03800   0.00000   1.00000   0.00000   0.00000
# Atom  O1                     0.00360  -0.10650   0.01410   0.00000   1.00000   0.00000   0.00000
# H   K   L     Mult    dspc                   |Fc|^2
   0    0    2     1      11.43050      0.69358575E+00
   2    0   -2     1       8.89791      0.74799341E+00
```

## 🔄 CIF Files

CIF (Crystallographic Information File) is the standard format for crystallographic data.

### File Extension
- **Extension**: `.cif`
- **Format**: Text-based, standardized
- **Standard**: IUCr CIF format

### Conversion to HKL

HKL3D uses the `cif2hkl` tool to convert CIF files to HKL format:

```bash
cif2hkl input.cif --output output.hkl
```

**Tool Source**: https://gitlab.com/soleil-data-treatment/soleil-software-projects/cif2hkl

## 📊 Data Validation

### Required Fields

For HKL files to work properly with HKL3D:

1. **Header**: TITLE, CELL, SPCGRP
2. **Atoms**: At least one atom with X, Y, Z coordinates
3. **Reflections**: At least one reflection with H, K, L, Mult, dspc, |Fc|²

### Format Validation

HKL3D validates:
- File extension (.hkl)
- Header structure
- Data column count
- Numerical value parsing
- Coordinate ranges

### Common Issues

#### 1. Missing Header
```
Error: Could not find the expected header in the file
```
**Solution**: Ensure file contains proper header section

#### 2. Incorrect Column Count
```
Error: Line parsing failed - incorrect number of columns
```
**Solution**: Check data section format matches header

#### 3. Invalid Coordinates
```
Warning: Invalid coordinate values detected
```
**Solution**: Verify X, Y, Z values are within [0, 1] for fractional coordinates

## 🔧 File Processing

### Reading Process

1. **File Open**: Check file exists and is readable
2. **Header Parsing**: Extract crystal parameters
3. **Atom Reading**: Parse atomic positions
4. **Reflection Loading**: Load HKL reflection data
5. **Data Validation**: Verify data integrity

### Memory Management

- **Efficient Loading**: Stream processing for large files
- **Data Structures**: Optimized NumPy arrays
- **Cleanup**: Proper memory deallocation

### Performance Considerations

- **File Size**: Typical HKL files: 1KB - 1MB
- **Reflection Count**: Usually 100 - 10,000 reflections
- **Atom Count**: Typically 10 - 1000 atoms
- **Processing Speed**: Sub-second loading for most files

## 📈 Data Analysis

### Statistical Information

HKL3D provides:
- **Reflection Count**: Total number of reflections
- **H, K, L Ranges**: Min/max values for each index
- **Intensity Distribution**: Min/max intensity values
- **d-spacing Range**: Min/max d-spacing values

### Quality Metrics

- **Completeness**: Percentage of expected reflections
- **Resolution**: Minimum d-spacing
- **Signal-to-Noise**: Intensity statistics
- **Symmetry**: Space group validation

## 🚀 Advanced Features

### Batch Processing

```bash
# Process multiple files
for file in *.hkl; do
    python3 hkl_reflections.py "$file" &
done
```

### Data Export

HKL3D can export:
- **Filtered Data**: Selected HKL ranges
- **Statistics**: Summary of data properties
- **Plots**: High-resolution images
- **Reports**: Text summaries

### Integration

- **External Tools**: cif2hkl, other crystallographic software
- **Data Pipelines**: Automated processing workflows
- **Format Conversion**: HKL ↔ CIF ↔ other formats

## 🐛 Troubleshooting

### File Reading Issues

1. **Permission Denied**: Check file permissions
2. **File Not Found**: Verify file path
3. **Encoding Issues**: Ensure ASCII/UTF-8 encoding
4. **Corrupted Data**: Validate file integrity

### Data Display Issues

1. **No Reflections**: Check data section format
2. **Wrong Coordinates**: Verify coordinate system
3. **Missing Atoms**: Check atom section format
4. **Invalid Values**: Validate numerical data

### Performance Issues

1. **Slow Loading**: Check file size and format
2. **Memory Errors**: Verify available RAM
3. **Display Lag**: Reduce data size or use filtering

## 📚 References

- **CIF Format**: International Union of Crystallography
- **HKL Format**: Crystallographica software
- **cif2hkl**: Synchrotron SOLEIL
- **Crystallography**: Basic crystallographic concepts

---

*Last updated: 2025*
