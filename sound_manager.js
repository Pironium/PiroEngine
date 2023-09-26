// Import the required modules for sound management
import AudioManager from 'audio-manager-library'; // Assume we have an external audio manager library

class SoundManager {
  constructor() {
    this.audioManager = new AudioManager();
    this.soundBank = new Map(); // Map to store loaded sounds
  }

  // Load a sound file
  loadSound(soundName, soundFilePath) {
    const sound = this.audioManager.loadSound(soundFilePath);
    this.soundBank.set(soundName, sound);
  }

  // Play a loaded sound
  playSound(soundName) {
    if (this.soundBank.has(soundName)) {
      const sound = this.soundBank.get(soundName);
      sound.play();
    } else {
      console.error(`Sound ${soundName} not found.`);
    }
  }

  // Stop a playing sound
  stopSound(soundName) {
    if (this.soundBank.has(soundName)) {
      const sound = this.soundBank.get(soundName);
      sound.stop();
    } else {
      console.error(`Sound ${soundName} not found.`);
    }
  }

  // Set volume for a specific sound
  setVolume(soundName, volume) {
    if (this.soundBank.has(soundName)) {
      const sound = this.soundBank.get(soundName);
      sound.setVolume(volume);
    } else {
      console.error(`Sound ${soundName} not found.`);
    }
  }
}

// Export the SoundManager class
export default SoundManager;
