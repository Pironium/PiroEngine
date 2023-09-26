-- enemy_ai.lua

-- Подключение библиотеки для работы с нейронными сетями
local neural_network = require("neural_network")

-- Функция для инициализации ИИ врагов
function initialize_enemy_ai(enemy)
    -- Создаем нейронную сеть
    local ai_brain = neural_network.create({
        input_neurons = 6,  -- 6 входных нейронов для восприятия окружающей среды
        hidden_layers = {8, 4}, -- 2 скрытых слоя с 8 и 4 нейронами соответственно
        output_neurons = 2  -- 2 выходных нейрона для управления врагом
    })

    -- Задаем начальные веса нейронной сети (случайные значения)
    ai_brain.initialize_weights()

    -- Функция для принятия решения на основе входных данных
    function enemy.make_decision(environment)
        -- Пропускаем данные через нейронную сеть
        local output = ai_brain.forward_propagate(environment)

        -- Принимаем решение на основе выходных данных
        local move_direction = output[1]  -- направление движения
        local fire_action = output[2]     -- действие стрельбы

        -- Возвращаем решение
        return move_direction, fire_action
    end

    return enemy
end

-- Функция обучения нейронной сети на основе опыта
function train_enemy_ai(ai_brain, training_data)
    -- Реализуем алгоритм обучения нейронной сети (например, обратное распространение ошибки)
    ai_brain.train(training_data)
end

-- Возвращаем модуль
return {
    initialize_enemy_ai = initialize_enemy_ai,
    train_enemy_ai = train_enemy_ai
}
