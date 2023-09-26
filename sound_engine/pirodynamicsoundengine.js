// PiroDynamicSoundEngine - A class to handle dynamic sound effects

class PiroDynamicSoundEngine {
  constructor() {
    this.soundBank = new Map(); // A map to store sound objects
  }

  // Load a sound file into the engine
  loadSound(soundName, soundFile) {
    const sound = new Audio(soundFile);
    this.soundBank.set(soundName, sound);
  }

  // Play a sound by name
  playSound(soundName) {
    const sound = this.soundBank.get(soundName);
    if (sound) {
      sound.currentTime = 0; // Rewind the sound to the beginning
      sound.play();
    }
  }

  // Stop a playing sound
  stopSound(soundName) {
    const sound = this.soundBank.get(soundName);
    if (sound) {
      sound.pause();
    }
  }

  // Set the volume of a sound
  setVolume(soundName, volume) {
    const sound = this.soundBank.get(soundName);
    if (sound) {
      sound.volume = volume;
    }
  }

  // Crossfade between two sounds
  crossfadeSounds(soundName1, soundName2, duration) {
    const sound1 = this.soundBank.get(soundName1);
    const sound2 = this.soundBank.get(soundName2);

    if (sound1 && sound2) {
      sound1.volume = 1;
      sound2.volume = 0;
      sound2.play();

      const step = 0.05;
      const interval = duration / (1 / step);

      const fade = () => {
        const currentVolume1 = sound1.volume;
        const currentVolume2 = sound2.volume;

        if (currentVolume1 > step) {
          sound1.volume = currentVolume1 - step;
          sound2.volume = currentVolume2 + step;

          setTimeout(fade, interval);
        } else {
          sound1.volume = 0;
          sound2.volume = 1;
        }
      };

      fade();
    }
  }
}

// Usage example:
const soundEngine = new PiroDynamicSoundEngine();
soundEngine.loadSound("explosion", "explosion.mp3");
soundEngine.loadSound("background_music", "background_music.mp3");

soundEngine.playSound("background_music");
soundEngine.crossfadeSounds("background_music", "explosion", 2000);
