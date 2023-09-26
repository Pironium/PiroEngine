#include <iostream>
#include <thread>

// Функция, которая будет выполняться на каждом потоке
void processTask(int taskId) {
    std::cout << "Processing task " << taskId << " on CPU core " << std::this_thread::get_id() << std::endl;
    // Здесь выполняем оптимизированный код для задачи taskId
}

int main() {
    int numCores = std::thread::hardware_concurrency(); // Получаем количество доступных CPU ядер

    std::cout << "Detected " << numCores << " CPU cores." << std::endl;

    // Создаем массив потоков для выполнения задач
    std::thread threads[numCores];

    // Запускаем потоки для выполнения задач
    for (int i = 0; i < numCores; ++i) {
        threads[i] = std::thread(processTask, i);
    }

    // Ждем завершения всех потоков
    for (int i = 0; i < numCores; ++i) {
        threads[i].join();
    }

    std::cout << "All tasks completed." << std::endl;

    return 0;
}
