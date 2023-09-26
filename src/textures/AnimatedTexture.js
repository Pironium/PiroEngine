class AnimatedTexture {
  constructor(frames, frameDuration) {
    this.frames = frames; // Массив текстур для анимации
    this.frameDuration = frameDuration; // Длительность отображения каждого кадра
    this.currentFrame = 0; // Текущий кадр
    this.timeSinceLastFrame = 0; // Время, прошедшее с отображения текущего кадра
  }

  update(deltaTime) {
    // Обновляем текущий кадр на основе прошедшего времени
    this.timeSinceLastFrame += deltaTime;
    if (this.timeSinceLastFrame >= this.frameDuration) {
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
      this.timeSinceLastFrame = 0;
    }
  }

  render() {
    // Отображаем текущий кадр на экране
    const currentFrameTexture = this.frames[this.currentFrame];
    // Код для отображения текстуры на экране
  }
}
