// PiroEngine GUI Module
class PiroGUI {
  constructor() {
    this.elements = [];
    this.activeElement = null;
  }

  // Add a GUI element
  addElement(element) {
    this.elements.push(element);
  }

  // Set the active GUI element
  setActiveElement(element) {
    this.activeElement = element;
  }

  // Render all GUI elements
  render() {
    for (const element of this.elements) {
      element.render();
    }
  }
}

// GUI Element base class
class GUIElement {
  constructor(x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
  }

  // Render the GUI element (abstract method)
  render() {
    // This is an abstract method, must be implemented in derived classes
  }
}

// Button class
class Button extends GUIElement {
  constructor(x, y, width, height, text, onClick) {
    super(x, y, width, height);
    this.text = text;
    this.onClick = onClick;
  }

  // Render the button
  render() {
    // Render button appearance with HTML and CSS
    const buttonElement = document.createElement("button");
    buttonElement.style.position = "absolute";
    buttonElement.style.left = `${this.x}px`;
    buttonElement.style.top = `${this.y}px`;
    buttonElement.style.width = `${this.width}px`;
    buttonElement.style.height = `${this.height}px`;
    buttonElement.textContent = this.text;
    
    // Handle button click event
    buttonElement.addEventListener("click", () => {
      this.onClick();
    });

    // Append the button to the document
    document.body.appendChild(buttonElement);
  }
}

// Text label class
class Label extends GUIElement {
  constructor(x, y, text) {
    super(x, y, 0, 0); // Labels auto-size based on text
    this.text = text;
  }

  // Render the label
  render() {
    // Render label appearance with HTML and CSS
    const labelElement = document.createElement("div");
    labelElement.style.position = "absolute";
    labelElement.style.left = `${this.x}px`;
    labelElement.style.top = `${this.y}px`;
    labelElement.textContent = this.text;

    // Append the label to the document
    document.body.appendChild(labelElement);
  }
}

// Example usage:
const gui = new PiroGUI();

const startButton = new Button(20, 20, 100, 40, "Start Game", () => {
  // Start the game logic here
});

const scoreLabel = new Label(150, 20, "Score: 0");

gui.addElement(startButton);
gui.addElement(scoreLabel);

// Set the active element (for keyboard/gamepad navigation)
gui.setActiveElement(startButton);

// Render the GUI
gui.render();
