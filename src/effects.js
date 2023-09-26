// Функция для создания эффекта блеска на объекте
function addGlowEffect(object) {
  const glowIntensity = 0.5; // Интенсивность блеска
  const glowColor = 'rgba(255, 255, 255, 0.7)'; // Цвет блеска

  const glowShader = {
    uniforms: {
      c: { type: 'f', value: glowIntensity },
      p: { type: 'f', value: 5.0 },
      glowColor: { type: 'c', value: new THREE.Color(glowColor) },
      viewVector: { type: 'v3', value: camera.position }
    },
    vertexShader: `
      uniform vec3 viewVector;
      varying float intensity;
      void main() {
        vec3 vNormal = normalize(normalMatrix * normal);
        vec3 vView = normalize(viewVector - mvPosition.xyz);
        intensity = pow(glowIntensity - dot(vNormal, vView), p);
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      uniform vec3 glowColor;
      varying float intensity;
      void main() {
        vec3 glow = glowColor * intensity;
        gl_FragColor = vec4(glow, 1.0);
      }
    `
  };

  const glowMaterial = new THREE.ShaderMaterial(glowShader);
  const glowObject = new THREE.Mesh(object.geometry.clone(), glowMaterial);
  glowObject.position.copy(object.position);
  glowObject.scale.multiplyScalar(1.2); // Увеличим размер объекта для выделения блеском

  scene.add(glowObject); // Добавляем объект с эффектом блеска на сцену
}
