# PiroEngine Python Plugin Support

class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin_name):
        try:
            plugin = __import__(plugin_name)
            self.plugins.append(plugin)
            print(f"Loaded Python plugin: {plugin_name}")
        except ImportError as e:
            print(f"Failed to load Python plugin: {plugin_name}")
            print(f"Error: {e}")

    def execute_plugins(self):
        for plugin in self.plugins:
            plugin.execute()

# Example plugin usage:
if __name__ == "__main__":
    manager = PluginManager()
    manager.load_plugin("example_plugin")
    manager.execute_plugins()
