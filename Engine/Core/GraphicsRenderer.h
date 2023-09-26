#pragma once

class GraphicsRenderer {
public:
    virtual void Initialize() = 0;
    virtual void RenderScene() = 0;
    // Other rendering functions and features

protected:
    // Rendering data and algorithms
};
