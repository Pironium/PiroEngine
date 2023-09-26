#pragma once

#include "rendering/render_pass.h"

class DeferredShadingPass : public RenderPass {
public:
    DeferredShadingPass() {
        // Initialize deferred shading pass
        // ...
    }

    void execute(const RenderTarget& input, RenderTarget& output) {
        // Execute deferred shading pass
        // ...
    }
};
