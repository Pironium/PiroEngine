// PiroEngine 3D Physics Utility Library

class Vector3D {
  constructor(x, y, z) {
    this.x = x || 0;
    this.y = y || 0;
    this.z = z || 0;
  }

  add(otherVector) {
    this.x += otherVector.x;
    this.y += otherVector.y;
    this.z += otherVector.z;
  }

  subtract(otherVector) {
    this.x -= otherVector.x;
    this.y -= otherVector.y;
    this.z -= otherVector.z;
  }

  normalize() {
    const length = Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
    this.x /= length;
    this.y /= length;
    this.z /= length;
  }

  dotProduct(otherVector) {
    return this.x * otherVector.x + this.y * otherVector.y + this.z * otherVector.z;
  }

  crossProduct(otherVector) {
    return new Vector3D(
      this.y * otherVector.z - this.z * otherVector.y,
      this.z * otherVector.x - this.x * otherVector.z,
      this.x * otherVector.y - this.y * otherVector.x
    );
  }
}

class PhysicsObject {
  constructor(mass, position) {
    this.mass = mass || 1;
    this.position = position || new Vector3D();
    this.velocity = new Vector3D();
    this.acceleration = new Vector3D();
  }

  applyForce(force) {
    // F = ma
    this.acceleration.add(new Vector3D(force.x / this.mass, force.y / this.mass, force.z / this.mass));
  }

  update() {
    // Update position and velocity based on acceleration
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);

    // Reset acceleration
    this.acceleration = new Vector3D();
  }
}

// More physics utility functions can be added here.

module.exports = {
  Vector3D,
  PhysicsObject,
};
