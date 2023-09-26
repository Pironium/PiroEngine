import tensorflow as tf
import numpy as np

class AdvancedEnemyAI:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(self.input_size,), name='input'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.output_size, activation='softmax', name='output')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        return model

    def train(self, input_data, target_data):
        self.model.fit(input_data, target_data, epochs=10)

    def predict_action(self, state):
        state = np.array(state).reshape(1, self.input_size)
        action_probs = self.model.predict(state)[0]
        return np.random.choice(range(self.output_size), p=action_probs)

class Enemy:
    def __init__(self, ai):
        self.ai = ai

    def act(self, state):
        return self.ai.predict_action(state)

# Пример использования:
if __name__ == "__main__":
    input_size = 10
    output_size = 4
    ai = AdvancedEnemyAI(input_size, output_size)
    enemy = Enemy(ai)

    # Обучение AI на примерных данных
    input_data = np.random.rand(100, input_size)
    target_data = np.random.randint(output_size, size=(100,))
    target_data = tf.keras.utils.to_categorical(target_data, num_classes=output_size)

    ai.train(input_data, target_data)

    # Применение AI в игре
    game_state = np.random.rand(input_size)
    action = enemy.act(game_state)
    print("AI выбрало действие:", action)
