#include <iostream>
#include <string>

// Класс, представляющий игру
class Game {
public:
    Game(const std::string& name) : name(name) {}

    // Функция компиляции игры для заданной платформы
    void compileForPlatform(const std::string& platform) {
        std::cout << "Compiling game '" << name << "' for platform: " << platform << std::endl;
        // Здесь вы можете добавить уникальные шаги компиляции для PiroEngine
    }

private:
    std::string name;
};

int main() {
    // Создаем экземпляр игры
    Game awesomeGame("AwesomeGame");

    // Компилируем игру для различных платформ
    awesomeGame.compileForPlatform("Windows");
    awesomeGame.compileForPlatform("Android");
    awesomeGame.compileForPlatform("iPhone");
    awesomeGame.compileForPlatform("macOS");
    awesomeGame.compileForPlatform("Linux");
    awesomeGame.compileForPlatform("PS4");
    awesomeGame.compileForPlatform("Xbox One");

    return 0;
}
