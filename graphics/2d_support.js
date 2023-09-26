// PiroEngine - 2D Graphics Support

// Define a class for 2D sprites
class Sprite2D {
    constructor(imagePath) {
        this.image = new Image();
        this.image.src = imagePath;
        this.position = { x: 0, y: 0 };
    }

    setPosition(x, y) {
        this.position.x = x;
        this.position.y = y;
    }

    draw(context) {
        context.drawImage(this.image, this.position.x, this.position.y);
    }
}

// Define a class for 2D rendering context
class RenderContext2D {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.context = this.canvas.getContext('2d');
    }

    clear() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

// Example usage:
const canvasId = 'gameCanvas';
const renderer = new RenderContext2D(canvasId);
const sprite = new Sprite2D('path/to/your/2d/image.png');

function gameLoop() {
    renderer.clear();
    sprite.setPosition(100, 100);
    sprite.draw(renderer.context);
    requestAnimationFrame(gameLoop);
}

gameLoop();
