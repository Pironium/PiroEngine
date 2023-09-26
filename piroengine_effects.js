// Файл: piroengine_effects.js

// Функция для создания эффекта 3D вращения объекта
function apply3DRotationEffect(object, duration, degrees) {
  const keyframes = [
    { transform: 'rotateY(0deg)' },
    { transform: `rotateY(${degrees}deg)` }
  ];

  const options = {
    duration: duration,
    iterations: Infinity
  };

  const animation = object.animate(keyframes, options);

  return animation;
}

// Функция для создания эффекта мерцания объекта
function applyFlickerEffect(object, duration, intensity) {
  const keyframes = [
    { opacity: 1 },
    { opacity: intensity },
    { opacity: 1 }
  ];

  const options = {
    duration: duration,
    iterations: Infinity
  };

  const animation = object.animate(keyframes, options);

  return animation;
}

// Экспортируем функции для использования в PiroEngine
export { apply3DRotationEffect, applyFlickerEffect };
