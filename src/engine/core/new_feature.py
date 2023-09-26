# This is the implementation of a new feature in the PiroEngine

class NewFeature:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def perform_complex_operation(self, data):
        # This function performs a complex operation
        result = 0
        for value in data:
            result += value
        return result
