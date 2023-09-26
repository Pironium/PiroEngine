#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

// Define a custom macro to check CPU support for specific instruction set extensions
#define CHECK_CPU_SUPPORT(ext)                                        \
    static inline bool check_##ext##_support() {                       \
        uint32_t reg_eax = 0, reg_edx = 0;                             \
        asm volatile("cpuid"                                          \
                     : "=a"(reg_eax), "=d"(reg_edx)                    \
                     : "a"(1)                                         \
                     : "ebx", "ecx");                                  \
        return (reg_edx & (1 << 26)) != 0;                             \
    }

// Check for SSE2 support
CHECK_CPU_SUPPORT(sse2)

// Check for AVX support
CHECK_CPU_SUPPORT(avx)

// Check for SSE4.2 support
CHECK_CPU_SUPPORT(sse42)

// Function to initialize CPU support checks
void initialize_cpu_support() {
    printf("CPU Support for SSE2: %s\n", check_sse2_support() ? "Supported" : "Not Supported");
    printf("CPU Support for AVX: %s\n", check_avx_support() ? "Supported" : "Not Supported");
    printf("CPU Support for SSE4.2: %s\n", check_sse42_support() ? "Supported" : "Not Supported");
}

int main() {
    initialize_cpu_support();
    return 0;
}
