// text_fx_renderer.js

class TextFXRenderer {
  constructor() {
    this.textObjects = [];
  }

  addTextObject(text, position, color) {
    const textObject = {
      text,
      position,
      color,
      animationFrames: [],
    };

    this.textObjects.push(textObject);
    return textObject;
  }

  addAnimationToTextObject(textObject, animationFrames) {
    if (!this.textObjects.includes(textObject)) {
      throw new Error('Text object is not registered with TextFXRenderer');
    }

    textObject.animationFrames = animationFrames;
  }

  render() {
    for (const textObject of this.textObjects) {
      const { text, position, color, animationFrames } = textObject;

      // Render the text at the specified position with color
      // Apply animations from animationFrames
      // ...

      console.log(`Rendering text: "${text}" at position ${position} with color ${color}`);
      console.log('Applying animation frames:', animationFrames);
      // Actual rendering and animation logic would go here
    }
  }
}

module.exports = TextFXRenderer;
