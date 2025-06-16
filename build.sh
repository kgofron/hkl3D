#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Build configuration
PROGRAM="read_hkl"
SOURCE="read_hkl.cpp"
COMPILER="g++"
FLAGS="-Wall -Wextra -std=c++11"

echo -e "${YELLOW}Starting build process...${NC}"

# Check if source file exists
if [ ! -f "$SOURCE" ]; then
    echo -e "${RED}Error: Source file '$SOURCE' not found!${NC}"
    exit 1
fi

# Check if compiler is available
if ! command -v $COMPILER &> /dev/null; then
    echo -e "${RED}Error: Compiler '$COMPILER' not found!${NC}"
    exit 1
fi

# Remove old executable if it exists
if [ -f "$PROGRAM" ]; then
    echo -e "${YELLOW}Removing old executable...${NC}"
    rm "$PROGRAM"
fi

# Compile the program
echo -e "${YELLOW}Compiling $SOURCE...${NC}"
$COMPILER $FLAGS -o "$PROGRAM" "$SOURCE"

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Build successful!${NC}"
    echo -e "${GREEN}Executable created: $PROGRAM${NC}"
    
    # Display file size
    SIZE=$(du -h "$PROGRAM" | cut -f1)
    echo -e "${GREEN}Executable size: $SIZE${NC}"
else
    echo -e "${RED}Build failed!${NC}"
    exit 1
fi

# Make the script executable
chmod +x "$PROGRAM"

echo -e "${YELLOW}Build process completed.${NC}" 