# Импорт необходимых библиотек
import tensorflow as tf
from tensorflow.keras import layers

# Определение нейронной сети для улучшения полигонов
def create_polygon_improvement_nn():
    # Создание модели Sequential
    model = tf.keras.Sequential()
    
    # Слой входных данных для полигонов
    model.add(layers.Input(shape=(3,)))  # Входные данные: координаты трех вершин полигона
    
    # Полносвязный слой для извлечения признаков
    model.add(layers.Dense(128, activation='relu'))
    
    # Добавление слоев для улучшения полигонов
    # (Можно добавить больше слоев или изменить параметры для улучшения производительности)
    
    # Полносвязный слой с активацией ReLU
    model.add(layers.Dense(256, activation='relu'))
    
    # Полносвязный слой с активацией ReLU
    model.add(layers.Dense(256, activation='relu'))
    
    # Полносвязный слой с активацией ReLU
    model.add(layers.Dense(128, activation='relu'))
    
    # Выходной слой, возвращающий улучшенные координаты полигонов
    model.add(layers.Dense(3))
    
    # Компиляция модели
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    return model

# Создание экземпляра нейронной сети
polygon_improvement_nn = create_polygon_improvement_nn()

# Вывод описания нейронной сети
polygon_improvement_nn.summary()
