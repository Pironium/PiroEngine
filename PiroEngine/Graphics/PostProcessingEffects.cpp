#include <iostream>
#include <vector>

class PostProcessingEffects {
private:
    std::vector<std::string> effects;

public:
    void addEffect(const std::string& effect) {
        effects.push_back(effect);
    }

    void applyEffects() {
        for (const auto& effect : effects) {
            std::cout << "Applying effect: " << effect << std::endl;
            // Code to apply the specified post-processing effect
        }
    }
};
