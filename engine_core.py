class PiroEngine:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, module):
        if module in self.modules:
            self.modules.remove(module)

    def run(self):
        for module in self.modules:
            module.execute()

class PiroModule:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing {self.name} module")

# Let's create some sample modules
module1 = PiroModule("Module1")
module2 = PiroModule("Module2")

# Create an instance of the engine and add modules
engine = PiroEngine()
engine.add_module(module1)
engine.add_module(module2)

# Run the engine
engine.run()
