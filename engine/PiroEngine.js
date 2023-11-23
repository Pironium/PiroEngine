class PiroEngine {
  constructor() {
    this.version = "1.0";
    this.features = [];
  }

  addFeature(feature) {
    this.features.push(feature);
  }

  start() {
    console.log("PiroEngine is starting...");
    console.log(`Version: ${this.version}`);
    console.log("Features:");
    this.features.forEach((feature) => {
      console.log(`- ${feature}`);
    });
    console.log("PiroEngine is ready to use!");
  }
}

module.exports = PiroEngine;
