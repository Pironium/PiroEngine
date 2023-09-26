# PiroEngine GUI Features
# This file contains unique GUI features for the PiroEngine game engine.

class PiroEngineGUI:
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        self.elements = []

    def create_button(self, label, x, y, width, height):
        """
        Create a clickable button element in the GUI.

        Args:
            label (str): The text label of the button.
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.

        Returns:
            Button: An instance of the Button class.
        """
        button = Button(label, x, y, width, height)
        self.elements.append(button)
        return button

    def create_slider(self, label, x, y, width, height, min_value, max_value):
        """
        Create a slider element in the GUI.

        Args:
            label (str): The text label of the slider.
            x (int): The x-coordinate of the slider's top-left corner.
            y (int): The y-coordinate of the slider's top-left corner.
            width (int): The width of the slider.
            height (int): The height of the slider.
            min_value (int): The minimum value of the slider.
            max_value (int): The maximum value of the slider.

        Returns:
            Slider: An instance of the Slider class.
        """
        slider = Slider(label, x, y, width, height, min_value, max_value)
        self.elements.append(slider)
        return slider

    def create_textbox(self, x, y, width, height):
        """
        Create a textbox element in the GUI.

        Args:
            x (int): The x-coordinate of the textbox's top-left corner.
            y (int): The y-coordinate of the textbox's top-left corner.
            width (int): The width of the textbox.
            height (int): The height of the textbox.

        Returns:
            Textbox: An instance of the Textbox class.
        """
        textbox = Textbox(x, y, width, height)
        self.elements.append(textbox)
        return textbox

class Button:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False

    def click(self):
        self.clicked = True

class Slider:
    def __init__(self, label, x, y, width, height, min_value, max_value):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value

    def set_value(self, value):
        if self.min_value <= value <= self.max_value:
            self.value = value

class Textbox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ""

    def set_text(self, text):
        self.text = text
