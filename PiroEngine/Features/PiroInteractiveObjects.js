class PiroInteractiveObject {
  constructor() {
    this.interactions = [];
  }

  addInteraction(interaction) {
    this.interactions.push(interaction);
  }

  interact() {
    for (const interaction of this.interactions) {
      interaction.execute();
    }
  }
}

class PiroInteraction {
  constructor(description, action) {
    this.description = description;
    this.action = action;
  }

  execute() {
    console.log(`Performing interaction: ${this.description}`);
    this.action();
  }
}

// Example usage:
const interactiveObject = new PiroInteractiveObject();
const openDoorInteraction = new PiroInteraction("Open the door", () => {
  console.log("The door is now open.");
});

interactiveObject.addInteraction(openDoorInteraction);
interactiveObject.interact();
