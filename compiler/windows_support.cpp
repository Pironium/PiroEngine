#include <iostream>
#include <string>

class WindowsCompiler {
public:
    WindowsCompiler() {}

    void compileGame(std::string gameName) {
        std::cout << "Compiling game for Windows: " << gameName << std::endl;
        // Добавьте здесь код для компиляции игры под Windows
    }
};

int main() {
    WindowsCompiler compiler;
    std::string gameName = "MyAwesomeGame";
    compiler.compileGame(gameName);
    return 0;
}
