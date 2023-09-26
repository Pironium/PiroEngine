#include <iostream>

class DimensionSupport {
public:
    void addDimension(int dimension) {
        std::cout << "Added support for " << dimension << "D games and movies." << std::endl;
    }
};

int main() {
    DimensionSupport support;
    int dimensions[] = {2, 3, 4, 5, 6, 7, 9999};

    for (int i = 0; i < sizeof(dimensions) / sizeof(dimensions[0]); ++i) {
        support.addDimension(dimensions[i]);
    }

    return 0;
}
