// Import necessary modules
import { Object3D, AnimationMixer, AnimationClip } from 'piroengine';

// Define a class for animated objects
class AnimatedObject extends Object3D {
  constructor(geometry, material) {
    super(geometry, material);

    // Create an AnimationMixer
    this.mixer = new AnimationMixer(this);

    // Initialize an empty array to store animation clips
    this.animationClips = [];
  }

  // Add a new animation clip to the object
  addAnimationClip(name, keyframes) {
    const clip = new AnimationClip(name, keyframes);
    this.animationClips.push(clip);
  }

  // Play a specific animation clip
  playAnimation(name) {
    const clip = this.animationClips.find(clip => clip.name === name);
    if (clip) {
      const action = this.mixer.clipAction(clip);
      action.play();
    }
  }
}

// Export the AnimatedObject class
export { AnimatedObject };
