// PiroEngine - Unique ID Generator

// Generate a unique ID for game objects
function generateUniqueId() {
  const timestamp = Date.now().toString(36); // Convert current timestamp to base36
  const randomChars = Math.random().toString(36).substring(2, 10); // Generate random characters
  return `${timestamp}${randomChars}`.toUpperCase(); // Combine timestamp and random characters
}

module.exports = {
  generateUniqueId,
};
