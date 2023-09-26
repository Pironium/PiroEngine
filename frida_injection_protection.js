// Директория, в которой будет файл/frida_injection_protection.js

// Функция, которая будет отслеживать попытки инъекции с помощью Frida
function monitorFridaInjection() {
    const fridaLibraryName = "frida.so"; // Название библиотеки Frida

    // Получаем список всех загруженных библиотек
    const loadedLibraries = Process.enumerateModules();

    for (const module of loadedLibraries) {
        if (module.name.includes(fridaLibraryName)) {
            // Обнаружена попытка инъекции Frida
            console.log("Frida injection attempt detected!");
            // Можем принимать различные меры, например, завершить работу приложения
            Process.exit(1);
        }
    }
}

// Запускаем мониторинг инъекций при старте движка
function initializeFridaInjectionProtection() {
    console.log("Initializing Frida injection protection...");
    // Запускаем мониторинг инъекций в отдельном потоке
    setImmediate(monitorFridaInjection);
}

// Вызываем функцию инициализации защиты при запуске движка
initializeFridaInjectionProtection();
