#include <iostream>
#include <string>
#include <vector>

class PlatformCompiler {
public:
    PlatformCompiler() {}

    // Function to compile the game for Windows
    void CompileForWindows(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for Windows..." << std::endl;
        // Implementation for compiling on Windows
    }

    // Function to compile the game for Android
    void CompileForAndroid(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for Android..." << std::endl;
        // Implementation for compiling on Android
    }

    // Function to compile the game for iPhone
    void CompileForiPhone(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for iPhone..." << std::endl;
        // Implementation for compiling on iPhone
    }

    // Function to compile the game for macOS
    void CompileForMacOS(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for macOS..." << std::endl;
        // Implementation for compiling on macOS
    }

    // Function to compile the game for Linux
    void CompileForLinux(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for Linux..." << std::endl;
        // Implementation for compiling on Linux
    }

    // Function to compile the game for PS4
    void CompileForPS4(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for PS4..." << std::endl;
        // Implementation for compiling on PS4
    }

    // Function to compile the game for Xbox One
    void CompileForXboxOne(const std::string& gameName) {
        std::cout << "Compiling " << gameName << " for Xbox One..." << std::endl;
        // Implementation for compiling on Xbox One
    }
};

int main() {
    PlatformCompiler compiler;
    std::string gameName = "MyAwesomeGame";

    // Compile the game for various platforms
    compiler.CompileForWindows(gameName);
    compiler.CompileForAndroid(gameName);
    compiler.CompileForiPhone(gameName);
    compiler.CompileForMacOS(gameName);
    compiler.CompileForLinux(gameName);
    compiler.CompileForPS4(gameName);
    compiler.CompileForXboxOne(gameName);

    return 0;
}
