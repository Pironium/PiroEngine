// PiroEngine Physics Module

class Physics {
  constructor() {
    this.gravity = 9.81; // Earth's gravity constant (m/s^2)
  }

  applyGravity(object, deltaTime) {
    if (object.mass !== undefined) {
      // Calculate the force due to gravity
      const force = object.mass * this.gravity;
      
      // Apply the force to the object
      object.applyForce(0, -force);
    }
  }

  // More physics functions can be added here
}

export default Physics;
