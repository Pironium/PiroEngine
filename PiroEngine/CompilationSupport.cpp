#include <iostream>
#include <vector>
#include <string>

class GameCompiler {
public:
    // Constructor
    GameCompiler() {
        supportedPlatforms = {"Windows", "Android", "iPhone", "macOS", "Linux", "PS4", "Xbox One"};
    }

    // Compile the game for a specific platform
    void compileGame(const std::string& platform) {
        if (isPlatformSupported(platform)) {
            std::cout << "Compiling the game for " << platform << "..." << std::endl;
            // Add platform-specific compilation logic here
        } else {
            std::cout << "Platform " << platform << " is not supported." << std::endl;
        }
    }

    // Check if a platform is supported
    bool isPlatformSupported(const std::string& platform) {
        for (const std::string& supportedPlatform : supportedPlatforms) {
            if (supportedPlatform == platform) {
                return true;
            }
        }
        return false;
    }

private:
    std::vector<std::string> supportedPlatforms;
};

int main() {
    GameCompiler compiler;

    // Compile the game for various platforms
    compiler.compileGame("Windows");
    compiler.compileGame("Android");
    compiler.compileGame("iPhone");
    compiler.compileGame("macOS");
    compiler.compileGame("Linux");
    compiler.compileGame("PS4");
    compiler.compileGame("Xbox One");

    return 0;
}
