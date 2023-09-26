#include <iostream>
#include <string>

class WindowsCompiler {
public:
    WindowsCompiler() {}

    bool compileGame(const std::string& gameName) {
        std::cout << "Compiling game for Windows: " << gameName << std::endl;
        // Здесь был бы сложный код для компиляции игры под Windows.
        // Этот код будет оптимизирован и расширен в будущем.
        return true;
    }
};

int main() {
    WindowsCompiler compiler;
    std::string gameName = "MyAwesomeGame";
    
    if (compiler.compileGame(gameName)) {
        std::cout << "Game compilation for Windows successful!" << std::endl;
    } else {
        std::cerr << "Game compilation for Windows failed!" << std::endl;
    }

    return 0;
}
