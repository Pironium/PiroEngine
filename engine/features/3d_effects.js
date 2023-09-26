// PiroEngine - Movie Maker 3D Effects Module
// This module provides advanced 3D effects for Movie Maker.

// Function to create a 3D explosion effect
function createExplosion(x, y, z) {
    // Generate a random pattern of particles to simulate explosion
    for (let i = 0; i < 1000; i++) {
        const particle = createParticle(x, y, z);
        particle.velocity.x = Math.random() * 10 - 5; // Random x velocity
        particle.velocity.y = Math.random() * 10 - 5; // Random y velocity
        particle.velocity.z = Math.random() * 10 - 5; // Random z velocity
        particle.color = getRandomColor(); // Random color for each particle
        MovieMaker.addParticle(particle);
    }
}

// Function to create a 3D particle
function createParticle(x, y, z) {
    return {
        position: { x, y, z },
        velocity: { x: 0, y: 0, z: 0 },
        color: "#FFFFFF",
        size: 5, // Size of the particle
        // Add more properties for customization as needed
    };
}

// Function to get a random color
function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Export the functions for use in Movie Maker
module.exports = {
    createExplosion,
    createParticle,
};
