import numpy as np
import sounddevice as sd

class AudioEngine:
    def __init__(self):
        self.sample_rate = 44100  # Задаем частоту дискретизации по умолчанию
        self.audio_buffer = np.zeros(0)

    def set_sample_rate(self, sample_rate):
        """Устанавливает частоту дискретизации для аудио"""
        self.sample_rate = sample_rate

    def load_audio(self, audio_data):
        """Загружает аудио данные в буфер"""
        self.audio_buffer = np.append(self.audio_buffer, audio_data)

    def play_audio(self):
        """Воспроизводит аудио из буфера"""
        sd.play(self.audio_buffer, self.sample_rate)
        sd.wait()

    def clear_buffer(self):
        """Очищает аудио буфер"""
        self.audio_buffer = np.zeros(0)
