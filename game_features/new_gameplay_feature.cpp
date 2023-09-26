#include <iostream>
#include <vector>
#include <cmath>

class NewGameplayFeature {
private:
    std::vector<float> gameData;

public:
    explicit NewGameplayFeature(const std::vector<float>& data) : gameData(data) {}

    float calculateGameScore() {
        float score = 0.0;
        for (const auto& value : gameData) {
            score += std::sqrt(value);  // Perform complex calculations for gameplay score
        }
        return score;
    }
};

int main() {
    // Simulate usage of the new gameplay feature
    std::vector<float> gameData = {10.0, 15.0, 20.0, 25.0};
    NewGameplayFeature gameplayFeature(gameData);
    float score = gameplayFeature.calculateGameScore();
    std::cout << "Gameplay score: " << score << std::endl;

    return 0;
}
