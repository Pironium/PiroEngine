#include <iostream>
#include <vector>
#include <cuda_runtime.h>
#include <CL/cl.h>

// Функция для инициализации CUDA
void initCUDA() {
    cudaDeviceProp prop;
    int count;
    cudaGetDeviceCount(&count);

    if (count == 0) {
        std::cerr << "No CUDA-capable devices found." << std::endl;
        exit(EXIT_FAILURE);
    }

    int device = 0;
    cudaGetDeviceProperties(&prop, device);

    std::cout << "Using CUDA device: " << prop.name << std::endl;
}

// Функция для инициализации OpenCL
void initOpenCL() {
    cl_platform_id platform;
    clGetPlatformIDs(1, &platform, nullptr);

    cl_device_id device;
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, nullptr);

    char device_name[128];
    clGetDeviceInfo(device, CL_DEVICE_NAME, sizeof(device_name), device_name, nullptr);

    std::cout << "Using OpenCL device: " << device_name << std::endl;
}

int main() {
    // Инициализация CUDA и OpenCL
    initCUDA();
    initOpenCL();

    // Здесь идет ваша сложная и длинная логика рендеринга с использованием CUDA и OpenCL

    return 0;
}
