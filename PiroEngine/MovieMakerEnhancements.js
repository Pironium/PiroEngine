// MovieMakerEnhancements.js

// Import necessary modules
import PiroEngine from './PiroEngine';

/**
 * Function to add 3D camera support to Movie Maker
 * @param {Object} cameraConfig - Configuration for the camera
 */
function add3DCameraSupport(cameraConfig) {
  // Check if the Movie Maker instance exists
  if (!PiroEngine.MovieMaker) {
    console.error('Movie Maker is not initialized.');
    return;
  }

  // Create a 3D camera with the provided configuration
  const camera = new PiroEngine.Camera3D(cameraConfig);

  // Add the camera to the Movie Maker
  PiroEngine.MovieMaker.addCamera(camera);
}

/**
 * Function to add special effects to Movie Maker
 * @param {string} effectType - Type of special effect to add
 * @param {Object} effectConfig - Configuration for the effect
 */
function addSpecialEffect(effectType, effectConfig) {
  // Check if the Movie Maker instance exists
  if (!PiroEngine.MovieMaker) {
    console.error('Movie Maker is not initialized.');
    return;
  }

  // Create a special effect based on the provided type and configuration
  const effect = PiroEngine.createSpecialEffect(effectType, effectConfig);

  // Add the effect to the Movie Maker
  PiroEngine.MovieMaker.addSpecialEffect(effect);
}

// Export the functions for use in PiroEngine
export { add3DCameraSupport, addSpecialEffect };
