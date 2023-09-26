// Функция для создания GUI элементов на HTML и стилизации через CSS
function createGUIElement(tagName, id, className) {
  const element = document.createElement(tagName);
  element.id = id;
  element.className = className;
  return element;
}

// Функция для добавления CSS стилей к элементу
function addCSSStyle(element, propertyName, propertyValue) {
  element.style[propertyName] = propertyValue;
}

// Класс для управления GUI
class GUISupport {
  constructor() {
    this.elements = []; // Список GUI элементов
  }

  // Метод для добавления GUI элемента
  addGUIElement(tagName, id, className) {
    const element = createGUIElement(tagName, id, className);
    this.elements.push(element);
    return element;
  }

  // Метод для установки CSS стилей для GUI элемента
  setCSSStyles(element, styles) {
    for (const [propertyName, propertyValue] of Object.entries(styles)) {
      addCSSStyle(element, propertyName, propertyValue);
    }
  }
}

// Пример использования:
const guiSupport = new GUISupport();
const button = guiSupport.addGUIElement('button', 'myButton', 'btn-primary');
guiSupport.setCSSStyles(button, {
  width: '100px',
  height: '40px',
  backgroundColor: 'blue',
  color: 'white',
});

// Добавляем кнопку в DOM
document.body.appendChild(button);
