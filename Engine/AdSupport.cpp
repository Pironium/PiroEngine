#include "AdSupport.h"
#include <iostream>

// Рекламный модуль для инициализации и показа рекламы
class AdModule {
public:
    void Initialize() {
        // Здесь инициализируется сторонний рекламный модуль
        std::cout << "Рекламный модуль инициализирован." << std::endl;
    }

    void ShowAd() {
        // Здесь будет код для отображения рекламы
        std::cout << "Реклама отображена." << std::endl;
    }
};

// Глобальный объект рекламного модуля
AdModule g_AdModule;

// Функция для инициализации рекламы
void InitializeAds() {
    g_AdModule.Initialize();
}

// Функция для показа рекламы
void ShowAds() {
    g_AdModule.ShowAd();
}
