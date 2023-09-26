#include <iostream>
#include <vector>

class NewFeature {
public:
    NewFeature() {
        std::cout << "Initializing New Feature..." << std::endl;
    }

    void performAction() {
        std::cout << "Performing a complex action using the New Feature." << std::endl;
    }

    std::vector<int> generateUniqueData() {
        std::vector<int> data;
        for (int i = 0; i < 1000; ++i) {
            data.push_back(i * 2);
        }
        return data;
    }
};
