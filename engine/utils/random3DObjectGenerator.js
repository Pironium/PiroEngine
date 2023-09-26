function random3DObjectGenerator() {
  // Генерация случайных координат для объекта
  const x = Math.random() * 100;
  const y = Math.random() * 100;
  const z = Math.random() * 100;

  // Генерация случайного цвета объекта
  const color = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;

  // Создание трехмерного объекта
  const object = {
    position: { x, y, z },
    color,
    // Другие свойства объекта, такие как размер, форма и текстура, могут быть добавлены здесь
  };

  return object;
}
