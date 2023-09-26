# PiroEngine Map Maker Module

class Map:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        else:
            return None

class Tile:
    def __init__(self, texture):
        self.texture = texture

class MapMaker:
    def __init__(self):
        self.maps = []

    def create_map(self, name, width, height):
        new_map = Map(name, width, height)
        self.maps.append(new_map)
        return new_map

    def export_map(self, map_obj, filename):
        with open(filename, 'w') as file:
            file.write(f"Map: {map_obj.name}\n")
            file.write(f"Dimensions: {map_obj.width}x{map_obj.height}\n")
            for row in map_obj.tiles:
                for tile in row:
                    if tile:
                        file.write(tile.texture)
                    else:
                        file.write(" ")
                file.write("\n")

# Example usage
if __name__ == "__main__":
    map_maker = MapMaker()
    game_map = map_maker.create_map("Level 1", 10, 10)

    for y in range(5):
        for x in range(5):
            game_map.set_tile(x, y, Tile("X"))

    map_maker.export_map(game_map, "level1.txt")
