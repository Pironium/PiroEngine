// PiroEngine GUI Module

class PiroGUI {
  constructor() {
    this.elements = [];
  }

  // Create a new GUI element
  createGUIElement(type, id, parent) {
    const element = document.createElement(type);
    element.id = id;
    parent.appendChild(element);
    this.elements.push(element);
    return element;
  }

  // Add a button to the GUI
  addButton(id, text, parent) {
    const button = this.createGUIElement("button", id, parent);
    button.textContent = text;
    return button;
  }

  // Add a text input field to the GUI
  addTextInput(id, parent) {
    const input = this.createGUIElement("input", id, parent);
    input.type = "text";
    return input;
  }

  // Add a label to the GUI
  addLabel(id, text, parent) {
    const label = this.createGUIElement("label", id, parent);
    label.textContent = text;
    return label;
  }

  // Add a custom 3D model viewer to the GUI
  addModelViewer(id, parent) {
    // Code for integrating a 3D model viewer here
    const modelViewer = this.createGUIElement("div", id, parent);
    modelViewer.textContent = "3D Model Viewer Placeholder";
    return modelViewer;
  }

  // Add a custom particle system editor to the GUI
  addParticleSystemEditor(id, parent) {
    // Code for integrating a particle system editor here
    const particleEditor = this.createGUIElement("div", id, parent);
    particleEditor.textContent = "Particle System Editor Placeholder";
    return particleEditor;
  }
}

// Export the PiroGUI class
export default PiroGUI;
