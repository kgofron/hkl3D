#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

struct HKLData {
    int h, k, l;
    int multiplicity;
    double dspacing;
    double fc_squared;
};

bool has_hkl_extension(const std::string& filename) {
    if (filename.length() < 4) return false;
    return filename.substr(filename.length() - 4) == ".hkl";
}

void print_usage(const char* program_name) {
    std::cerr << "Usage: " << program_name << " <filename.hkl>" << std::endl;
    std::cerr << "Example: " << program_name << " EntryWithCollCode176.hkl" << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        print_usage(argv[0]);
        return 1;
    }

    std::string filename = argv[1];
    if (!has_hkl_extension(filename)) {
        std::cerr << "Error: File must have .hkl extension" << std::endl;
        print_usage(argv[0]);
        return 1;
    }

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return 1;
    }

    std::string line;
    bool found_header = false;
    std::vector<HKLData> hkl_data;

    // Read until we find the header
    while (std::getline(file, line)) {
        if (line.find("# H   K   L     Mult    dspc                   |Fc|^2") != std::string::npos) {
            found_header = true;
            break;
        }
    }

    if (!found_header) {
        std::cerr << "Error: Could not find the expected header in the file" << std::endl;
        file.close();
        return 1;
    }

    // Read the data lines
    while (std::getline(file, line)) {
        // Skip empty lines or lines starting with #
        if (line.empty() || line[0] == '#') continue;

        std::istringstream iss(line);
        HKLData data;
        
        if (iss >> data.h >> data.k >> data.l >> data.multiplicity >> data.dspacing >> data.fc_squared) {
            hkl_data.push_back(data);
        }
    }

    // Print the data
    std::cout << "Found " << hkl_data.size() << " reflections:" << std::endl;
    for (const auto& data : hkl_data) {
        std::cout << "H: " << data.h 
                  << " K: " << data.k 
                  << " L: " << data.l 
                  << " Mult: " << data.multiplicity 
                  << " d-spacing: " << data.dspacing 
                  << " |Fc|^2: " << data.fc_squared << std::endl;
    }

    file.close();
    return 0;
} 