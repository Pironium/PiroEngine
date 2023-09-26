// Importing necessary libraries and modules
import React from 'react';
import ThreeJS from 'three';

// Creating a class for the 3D view component
class ThreeDView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      // Initialize 3D scene, camera, and renderer
      scene: new ThreeJS.Scene(),
      camera: new ThreeJS.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000),
      renderer: new ThreeJS.WebGLRenderer(),
    };
  }

  componentDidMount() {
    // Append the 3D renderer to the component's DOM element
    this.state.renderer.setSize(window.innerWidth, window.innerHeight);
    this.mount.appendChild(this.state.renderer.domElement);

    // Create a cube and add it to the scene
    const geometry = new ThreeJS.BoxGeometry();
    const material = new ThreeJS.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new ThreeJS.Mesh(geometry, material);
    this.state.scene.add(cube);

    // Position the camera
    this.state.camera.position.z = 5;

    // Create an animation loop
    const animate = () => {
      requestAnimationFrame(animate);

      // Rotate the cube
      cube.rotation.x += 0.01;
      cube.rotation.y += 0.01;

      // Render the scene
      this.state.renderer.render(this.state.scene, this.state.camera);
    };

    // Start the animation loop
    animate();
  }

  render() {
    return (
      <div ref={(ref) => (this.mount = ref)}>
        {/* DOM element for the 3D renderer */}
      </div>
    );
  }
}

export default ThreeDView;
