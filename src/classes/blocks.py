from src.classes.Block import Block
from src.assets.textures import texture_sets
from src.assets.materials import materials

class Grass(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, texture_sets.grass, materials.Grass, 100)