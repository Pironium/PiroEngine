#pragma once

#include <iostream>
#include <vector>

class PostProcessingEffects {
private:
    std::vector<std::string> availableEffects;

public:
    PostProcessingEffects() {
        // Initialize available post-processing effects
        availableEffects.push_back("Bloom");
        availableEffects.push_back("DepthOfField");
        // Add more effects here...
    }

    void applyEffect(const std::string& effectName) {
        // Apply the specified post-processing effect
        if (std::find(availableEffects.begin(), availableEffects.end(), effectName) != availableEffects.end()) {
            std::cout << "Applying post-processing effect: " << effectName << std::endl;
            // Implement effect-specific code here...
        } else {
            std::cerr << "Effect not available: " << effectName << std::endl;
        }
    }
};
