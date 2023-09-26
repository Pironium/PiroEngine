class PiroEngine {
  constructor() {
    this.version = '1.0';
    this.modules = [];
  }

  addModule(module) {
    this.modules.push(module);
  }

  init() {
    this.modules.forEach(module => {
      module.setup();
    });
  }

  start() {
    console.log(`PiroEngine v${this.version} is starting...`);
    this.init();
    // Additional startup procedures
  }
}

module.exports = PiroEngine;
