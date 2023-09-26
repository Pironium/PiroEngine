# gpu_optimization.py

import piroscript as ps  # Импорт библиотеки PiroScript

# Функция для оптимизации под NVIDIA
def optimize_for_nvidia():
    with ps.cuda_thread as cuda:  # Используем CUDA поток
        cuda.enable_async_execution()  # Включаем асинхронное выполнение

        # Сложные вычисления, оптимизированные под NVIDIA
        result = cuda.parallel_compute(
            lambda x: x * x, range(10000)
        )

        return result

# Функция для оптимизации под AMD
def optimize_for_amd():
    with ps.opencl_thread as opencl:  # Используем OpenCL поток
        opencl.enable_double_precision()  # Включаем двойную точность

        # Сложные вычисления, оптимизированные под AMD
        result = opencl.parallel_compute(
            lambda x: x * x, range(10000)
        )

        return result

if __name__ == "__main__":
    nvidia_result = optimize_for_nvidia()
    amd_result = optimize_for_amd()

    print("Optimization for NVIDIA result:", nvidia_result)
    print("Optimization for AMD result:", amd_result)
