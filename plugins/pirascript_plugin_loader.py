import os
import importlib.util

class PiroScriptPluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.loaded_plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_directory):
            if filename.endswith(".pis"):
                plugin_name = os.path.splitext(filename)[0]
                plugin_module = self.load_plugin_module(plugin_name, os.path.join(self.plugin_directory, filename))
                if plugin_module:
                    self.loaded_plugins[plugin_name] = plugin_module

    def load_plugin_module(self, plugin_name, plugin_path):
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        if spec:
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)
            return plugin_module
        return None

    def run_plugin(self, plugin_name, *args, **kwargs):
        if plugin_name in self.loaded_plugins:
            plugin_module = self.loaded_plugins[plugin_name]
            if hasattr(plugin_module, "run"):
                return plugin_module.run(*args, **kwargs)
            else:
                raise AttributeError(f"Plugin '{plugin_name}' does not have a 'run' function.")
        else:
            raise ImportError(f"Plugin '{plugin_name}' not found or not loaded.")

# Пример использования
if __name__ == "__main__":
    plugin_loader = PiroScriptPluginLoader("plugins_directory")
    plugin_loader.load_plugins()
    result = plugin_loader.run_plugin("example_plugin", param1, param2)
    print(result)
