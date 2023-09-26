#include <iostream>
#include <vector>
#include <algorithm>

// Forward declarations for compatibility with NVIDIA and AMD GPUs.
namespace GPUOptimizations {
    class NvidiaOptimization;
    class AMDOptimization;
}

using namespace GPUOptimizations;

class BaseOptimization {
public:
    virtual void optimize() = 0;
};

class NvidiaOptimization : public BaseOptimization {
private:
    void specificOptimizations() {
        // Placeholder for NVIDIA-specific optimizations.
        // For instance, making use of specific CUDA kernels, etc.
    }
    
public:
    void optimize() override {
        specificOptimizations();
        std::cout << "NVIDIA GPU optimization applied." << std::endl;
    }
};

class AMDOptimization : public BaseOptimization {
private:
    void specificOptimizations() {
        // Placeholder for AMD-specific optimizations.
        // Like utilizing specific Vulkan API features.
    }
    
public:
    void optimize() override {
        specificOptimizations();
        std::cout << "AMD GPU optimization applied." << std::endl;
    }
};

class GraphicsEngine {
private:
    std::vector<BaseOptimization*> optimizations;

public:
    void addOptimization(BaseOptimization* opt) {
        optimizations.push_back(opt);
    }

    void applyOptimizations() {
        for (auto& opt : optimizations) {
            opt->optimize();
        }
    }
};

int main() {
    GraphicsEngine engine;

    NvidiaOptimization nvidiaOpt;
    AMDOptimization amdOpt;

    engine.addOptimization(&nvidiaOpt);
    engine.addOptimization(&amdOpt);
    engine.applyOptimizations();

    return 0;
}
