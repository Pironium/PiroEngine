// Директория: engine/
// Название файла: piroengine_optimization.c

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <immintrin.h> // Для использования SIMD инструкций

// Функция оптимизации для процессоров Intel и AMD
void optimizeForProcessors() {
    int numElements = 10000;
    float* data = (float*)malloc(sizeof(float) * numElements);

    // Инициализируем массив данными
    for (int i = 0; i < numElements; ++i) {
        data[i] = i * 2.0f;
    }

    // Выполняем вычисления с использованием SIMD инструкций
    __m256 sum = _mm256_setzero_ps();
    for (int i = 0; i < numElements; i += 8) {
        __m256 vec = _mm256_loadu_ps(&data[i]);
        sum = _mm256_add_ps(sum, vec);
    }

    // Вычисляем сумму элементов массива
    float result[8];
    _mm256_storeu_ps(result, sum);
    float totalSum = result[0] + result[1] + result[2] + result[3] + result[4] + result[5] + result[6] + result[7];

    printf("Total sum: %f\n", totalSum);

    free(data);
}

int main() {
    optimizeForProcessors();
    return 0;
}
