#include <stdio.h>
#include <stdlib.h>

// Функция компиляции игры для Windows
void compileForWindows(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for Windows...\n", gameName);
    // Ваш сложный код для компиляции игры под Windows
}

// Функция компиляции игры для Android
void compileForAndroid(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for Android...\n", gameName);
    // Ваш сложный код для компиляции игры под Android
}

// Функция компиляции игры для iPhone
void compileForiPhone(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for iPhone...\n", gameName);
    // Ваш сложный код для компиляции игры под iPhone
}

// Функция компиляции игры для macOS
void compileForMacOS(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for macOS...\n", gameName);
    // Ваш сложный код для компиляции игры под macOS
}

// Функция компиляции игры для Linux
void compileForLinux(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for Linux...\n", gameName);
    // Ваш сложный код для компиляции игры под Linux
}

// Функция компиляции игры для PS4
void compileForPS4(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for PS4...\n", gameName);
    // Ваш сложный код для компиляции игры под PS4
}

// Функция компиляции игры для Xbox One
void compileForXboxOne(const char* gameName, const char* sourceCode) {
    printf("Compiling game '%s' for Xbox One...\n", gameName);
    // Ваш сложный код для компиляции игры под Xbox One
}

int main() {
    const char* gameName = "MyGame";
    const char* sourceCode = "/* Your game source code here */";

    compileForWindows(gameName, sourceCode);
    compileForAndroid(gameName, sourceCode);
    compileForiPhone(gameName, sourceCode);
    compileForMacOS(gameName, sourceCode);
    compileForLinux(gameName, sourceCode);
    compileForPS4(gameName, sourceCode);
    compileForXboxOne(gameName, sourceCode);

    return 0;
}
