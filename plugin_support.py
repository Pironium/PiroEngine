# plugin_support.py

class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin_path):
        try:
            if plugin_path.endswith(".pis"):
                # Загрузка плагина на PiroScript
                plugin = self.load_piroscript_plugin(plugin_path)
            elif plugin_path.endswith(".lua"):
                # Загрузка плагина на Lua
                plugin = self.load_lua_plugin(plugin_path)
            else:
                raise ValueError("Unsupported plugin format")
            self.plugins.append(plugin)
            return True
        except Exception as e:
            print(f"Failed to load plugin '{plugin_path}': {e}")
            return False

    def load_piroscript_plugin(self, plugin_path):
        # Здесь может быть код для загрузки PiroScript плагина
        pass

    def load_lua_plugin(self, plugin_path):
        # Здесь может быть код для загрузки Lua плагина
        pass

    def run_plugins(self):
        for plugin in self.plugins:
            plugin.run()

class PiroScriptPlugin:
    def __init__(self, script_path):
        self.script_path = script_path

    def run(self):
        # Здесь может быть код выполнения PiroScript плагина
        pass

class LuaPlugin:
    def __init__(self, script_path):
        self.script_path = script_path

    def run(self):
        # Здесь может быть код выполнения Lua плагина
        pass

if __name__ == "__main__":
    plugin_manager = PluginManager()
    # Загрузка плагинов
    plugin_manager.load_plugin("example_plugin.pis")
    plugin_manager.load_plugin("another_plugin.lua")

    # Запуск плагинов
    plugin_manager.run_plugins()
