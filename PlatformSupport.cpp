#include <iostream>

// Define platform-specific macros
#define WINDOWS_SUPPORT_ENABLED
#define ANDROID_SUPPORT_ENABLED
#define IPHONE_SUPPORT_ENABLED
#define MACOS_SUPPORT_ENABLED
#define LINUX_SUPPORT_ENABLED
#define PS4_SUPPORT_ENABLED
#define XBOX_ONE_SUPPORT_ENABLED

// Function to check if PiroEngine supports a specific platform
bool IsPlatformSupported(const std::string& platform) {
    #ifdef WINDOWS_SUPPORT_ENABLED
    if (platform == "Windows") return true;
    #endif
    
    #ifdef ANDROID_SUPPORT_ENABLED
    if (platform == "Android") return true;
    #endif
    
    #ifdef IPHONE_SUPPORT_ENABLED
    if (platform == "iPhone") return true;
    #endif
    
    #ifdef MACOS_SUPPORT_ENABLED
    if (platform == "macOS") return true;
    #endif
    
    #ifdef LINUX_SUPPORT_ENABLED
    if (platform == "Linux") return true;
    #endif
    
    #ifdef PS4_SUPPORT_ENABLED
    if (platform == "PS4") return true;
    #endif
    
    #ifdef XBOX_ONE_SUPPORT_ENABLED
    if (platform == "Xbox One") return true;
    #endif
    
    return false;
}

int main() {
    std::string platformToCheck = "Windows";
    
    if (IsPlatformSupported(platformToCheck)) {
        std::cout << "PiroEngine supports " << platformToCheck << " platform." << std::endl;
    } else {
        std::cout << "PiroEngine does not support " << platformToCheck << " platform." << std::endl;
    }
    
    return 0;
}
