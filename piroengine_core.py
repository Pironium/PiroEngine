class PiroEngineCore:
    def __init__(self):
        self.engine = PiroEngine()

    def start(self):
        while True:
            self.engine.update()
