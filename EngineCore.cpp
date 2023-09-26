#include <iostream>
#include <string>

class PiroEngine {
public:
    PiroEngine() {
        std::cout << "Initializing PiroEngine..." << std::endl;
    }

    void CompileGameForWindows(const std::string& gameName) {
        std::cout << "Compiling game '" << gameName << "' for Windows..." << std::endl;
        // Здесь код для компиляции игры под Windows
    }
};

int main() {
    PiroEngine engine;
    engine.CompileGameForWindows("MyAwesomeGame");
    return 0;
}
