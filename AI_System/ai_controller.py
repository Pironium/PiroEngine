# PiroEngine AI Controller

class AIController:
    def __init__(self):
        self.npcs = []

    def add_npc(self, npc):
        self.npcs.append(npc)

    def update(self):
        for npc in self.npcs:
            npc.think()

class NPC:
    def __init__(self, name):
        self.name = name

    def think(self):
        # Здесь будет сложный код для искусственного интеллекта NPC
        pass
