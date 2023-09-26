#include "graphics/render_engine.h"
#include "graphics/nvidia_optimization.h"
#include "graphics/amd_optimization.h"

void RenderEngine::initialize() {
    // Initialize rendering engine
    // ...
}

void RenderEngine::renderFrame() {
    // Render frame using PiroScript
    // ...
    
    // Nvidia optimization
    NvidiaOptimization::applyOptimization();
    
    // Amd optimization
    AmdOptimization::applyOptimization();
    
    // ...
}
