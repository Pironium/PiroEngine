# PiroEngine_GUI.py

import tkinter as tk

class PiroEngineGUI:
    def __init__(self, root):
        self.root = root
        root.title("PiroEngine GUI")

        # Добавляем 3D виджет
        self.canvas_3d = tk.Canvas(root, width=800, height=600)
        self.canvas_3d.pack()

        # Добавляем кнопку для загрузки 3D моделей
        self.load_model_button = tk.Button(root, text="Загрузить 3D Модель")
        self.load_model_button.pack()

        # Добавляем панель инструментов для настроек
        self.tool_panel = tk.Frame(root)
        self.tool_panel.pack(side=tk.RIGHT)

        # Добавляем инструмент для управления камерой
        self.camera_control = tk.LabelFrame(self.tool_panel, text="Управление Камерой")
        self.camera_control.pack()

        # Добавляем ползунок для изменения положения камеры по X
        self.camera_x_slider = tk.Scale(self.camera_control, label="Положение X", from_=0, to=100)
        self.camera_x_slider.pack()

        # Добавляем ползунок для изменения положения камеры по Y
        self.camera_y_slider = tk.Scale(self.camera_control, label="Положение Y", from_=0, to=100)
        self.camera_y_slider.pack()

        # Добавляем ползунок для изменения положения камеры по Z
        self.camera_z_slider = tk.Scale(self.camera_control, label="Положение Z", from_=0, to=100)
        self.camera_z_slider.pack()

        # Добавляем кнопку для сохранения сцены
        self.save_scene_button = tk.Button(self.tool_panel, text="Сохранить Сцену")
        self.save_scene_button.pack()

        # Добавляем кнопку для загрузки сцены
        self.load_scene_button = tk.Button(self.tool_panel, text="Загрузить Сцену")
        self.load_scene_button.pack()

    def run(self):
        self.root.mainloop()

# Создаем главное окно приложения
root = tk.Tk()
app = PiroEngineGUI(root)
app.run()
