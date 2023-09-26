#include <PiroEngine.h>
#include <vulkan/vulkan.h>

// Функция оптимизации рендеринга с использованием Vulkan API
void OptimizeVulkanRendering(PiroEngineContext* context, VulkanRenderer* renderer) {
    // Получаем доступ к устройствам NVIDIA и AMD
    VkPhysicalDevice nvidiaDevice = renderer->GetNvidiaDevice();
    VkPhysicalDevice amdDevice = renderer->GetAmdDevice();

    // Проводим оптимизацию для NVIDIA
    if (nvidiaDevice != VK_NULL_HANDLE) {
        // Настройка параметров рендеринга для NVIDIA
        VkPhysicalDeviceFeatures nvidiaFeatures = {};
        nvidiaFeatures.geometryShader = VK_TRUE;
        nvidiaFeatures.tessellationShader = VK_TRUE;

        VkPhysicalDeviceProperties nvidiaProperties = {};
        vkGetPhysicalDeviceProperties(nvidiaDevice, &nvidiaProperties);
        nvidiaFeatures.limits.maxSamplerAnisotropy = nvidiaProperties.limits.maxSamplerAnisotropy;

        // Применяем настройки
        vkGetPhysicalDeviceFeatures(nvidiaDevice, &nvidiaFeatures);
    }

    // Проводим оптимизацию для AMD
    if (amdDevice != VK_NULL_HANDLE) {
        // Настройка параметров рендеринга для AMD
        VkPhysicalDeviceFeatures amdFeatures = {};
        amdFeatures.wideLines = VK_TRUE;

        VkPhysicalDeviceProperties amdProperties = {};
        vkGetPhysicalDeviceProperties(amdDevice, &amdProperties);
        amdFeatures.limits.maxSamplerAnisotropy = amdProperties.limits.maxSamplerAnisotropy;

        // Применяем настройки
        vkGetPhysicalDeviceFeatures(amdDevice, &amdFeatures);
    }
}
