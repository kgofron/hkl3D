CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11

TARGET = read_hkl
SRC = read_hkl.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)

.PHONY: all clean 