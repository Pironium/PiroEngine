# engine/plugins/plugin_loader.py

class PluginLoader:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin_path):
        try:
            with open(plugin_path, 'r') as plugin_file:
                plugin_code = plugin_file.read()
                plugin_module = compile(plugin_code, plugin_path, 'exec')
                exec(plugin_module, globals(), locals())
                self.plugins.append(locals())
                print(f"Loaded plugin from {plugin_path}")
        except Exception as e:
            print(f"Failed to load plugin from {plugin_path}: {str(e)}")

    def run_plugins(self):
        for plugin in self.plugins:
            if 'run' in plugin:
                try:
                    plugin['run']()
                except Exception as e:
                    print(f"Error executing plugin: {str(e)}")

if __name__ == "__main__":
    loader = PluginLoader()
    # Загрузка плагинов из директории 'plugins'
    plugin_directory = 'plugins/'
    plugin_files = ['plugin1.pis', 'plugin2.pis', 'plugin3.pis']  # Здесь указать реальные имена файлов
    for plugin_file in plugin_files:
        loader.load_plugin(plugin_directory + plugin_file)

    # Запуск загруженных плагинов
    loader.run_plugins()
