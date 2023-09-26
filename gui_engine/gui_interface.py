import tkinter as tk

class GameEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PiroEngine Game Editor")

        # Создаем меню
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Создаем меню "Файл"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть проект", command=self.open_project)
        self.file_menu.add_command(label="Сохранить проект", command=self.save_project)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=root.quit)

        # Создаем меню "Объекты"
        self.objects_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Объекты", menu=self.objects_menu)
        self.objects_menu.add_command(label="Создать объект", command=self.create_object)
        self.objects_menu.add_command(label="Редактировать объект", command=self.edit_object)
        self.objects_menu.add_command(label="Удалить объект", command=self.delete_object)

        # Создаем холст для редактирования сцен
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def open_project(self):
        # Здесь будет функциональность для открытия существующего проекта
        pass

    def save_project(self):
        # Здесь будет функциональность для сохранения текущего проекта
        pass

    def create_object(self):
        # Здесь будет функциональность для создания нового игрового объекта
        pass

    def edit_object(self):
        # Здесь будет функциональность для редактирования игрового объекта
        pass

    def delete_object(self):
        # Здесь будет функциональность для удаления игрового объекта
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GameEditor(root)
    root.mainloop()
