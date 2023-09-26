class PhysicsEngine {
  constructor() {
    this.gravity = 9.81; // Standard Earth gravity
  }

  applyGravity(object, time) {
    const force = object.mass * this.gravity;
    object.applyForce(0, -force, time);
  }

  // More physics methods here...
}

module.exports = PhysicsEngine;
