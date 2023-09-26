// PiroEngine Interactive Objects Module

class InteractiveObject {
    constructor(x, y, z) {
        this.position = { x, y, z };
        this.scale = 1.0;
        this.rotation = 0;
        this.animations = [];
    }

    setPosition(x, y, z) {
        this.position.x = x;
        this.position.y = y;
        this.position.z = z;
    }

    setScale(scale) {
        this.scale = scale;
    }

    setRotation(rotation) {
        this.rotation = rotation;
    }

    addAnimation(animation) {
        this.animations.push(animation);
    }

    playAnimations() {
        for (const animation of this.animations) {
            animation.play();
        }
    }

    update(deltaTime) {
        // Update object's state based on animations, user input, etc.
    }
}

class Animation {
    constructor(duration, keyframes) {
        this.duration = duration;
        this.keyframes = keyframes;
    }

    play() {
        // Play animation by interpolating keyframes over time
    }
}

export { InteractiveObject, Animation };
