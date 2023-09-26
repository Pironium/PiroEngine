import threading

class ResourceManager:
    def __init__(self):
        self.resource_map = {}
        self.lock = threading.Lock()

    def load_resource(self, resource_id, resource_path):
        with self.lock:
            if resource_id not in self.resource_map:
                # Simulate resource loading delay
                # In a real implementation, you would load the resource from file
                import time
                time.sleep(2)
                self.resource_map[resource_id] = resource_path

    def get_resource(self, resource_id):
        with self.lock:
            return self.resource_map.get(resource_id, None)

class ParallelResourceProcessor:
    def __init__(self):
        self.resource_manager = ResourceManager()

    def process_resource(self, resource_id, resource_path):
        # Load the resource in a separate thread
        thread = threading.Thread(target=self.resource_manager.load_resource, args=(resource_id, resource_path))
        thread.start()

    def get_processed_resource(self, resource_id):
        return self.resource_manager.get_resource(resource_id)
