#include <iostream>
#include "PiroEngine.h"

int main() {
    PiroEngine engine;
    engine.init();
    
    while (engine.isRunning()) {
        engine.update();
        engine.render();
    }
    
    engine.cleanup();
    return 0;
}
