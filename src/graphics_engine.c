#include <stdio.h>

// Структура для представления окна
struct Window {
    int width;
    int height;
    char* title;
};

// Функция для создания окна
struct Window* createWindow(int width, int height, const char* title) {
    struct Window* window = (struct Window*)malloc(sizeof(struct Window));
    window->width = width;
    window->height = height;
    window->title = strdup(title);
    return window;
}

// Функция для отображения окна
void renderWindow(struct Window* window) {
    printf("Rendering Window: %s (%d x %d)\n", window->title, window->width, window->height);
}

// Функция для освобождения ресурсов окна
void destroyWindow(struct Window* window) {
    free(window->title);
    free(window);
}
