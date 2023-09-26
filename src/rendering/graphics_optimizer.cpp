#include "graphics_optimizer.h"
#include <iostream>

namespace PiroEngine {

    // Функция для оптимизации графики под Nvidia и AMD
    void GraphicsOptimizer::OptimizeForGPU(const std::string& gpuManufacturer) {
        if (gpuManufacturer == "Nvidia") {
            // Оптимизация для Nvidia
            std::cout << "Optimizing graphics for Nvidia GPU..." << std::endl;
            // Добавьте здесь код для оптимизации под Nvidia
        }
        else if (gpuManufacturer == "AMD") {
            // Оптимизация для AMD
            std::cout << "Optimizing graphics for AMD GPU..." << std::endl;
            // Добавьте здесь код для оптимизации под AMD
        }
        else {
            std::cerr << "Unsupported GPU manufacturer: " << gpuManufacturer << std::endl;
        }
    }

}  // namespace PiroEngine
