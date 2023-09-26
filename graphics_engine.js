// Директория: engine/graphics_engine.js

// Подключение библиотеки для работы с 3D графикой
import * as ThreeJS from 'three.js';

// Класс для работы с 3D объектами
class Piro3DEngine {
  constructor() {
    this.scene = new ThreeJS.Scene();
    this.camera = new ThreeJS.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new ThreeJS.WebGLRenderer();
    
    // Установка размеров рендерера
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(this.renderer.domElement);
  }
  
  // Метод для добавления 3D объектов в сцену
  addObject(object) {
    this.scene.add(object);
  }
  
  // Метод для создания текстуры для объекта
  createTexture(imageUrl) {
    const textureLoader = new ThreeJS.TextureLoader();
    return textureLoader.load(imageUrl);
  }
  
  // Метод для рендеринга сцены
  render() {
    this.renderer.render(this.scene, this.camera);
  }
}

// Пример использования Piro3DEngine
const engine = new Piro3DEngine();
const cubeGeometry = new ThreeJS.BoxGeometry();
const cubeMaterial = new ThreeJS.MeshBasicMaterial({ map: engine.createTexture('cube_texture.jpg') });
const cube = new ThreeJS.Mesh(cubeGeometry, cubeMaterial);
engine.addObject(cube);

// Запуск рендеринга
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  engine.render();
}
animate();
