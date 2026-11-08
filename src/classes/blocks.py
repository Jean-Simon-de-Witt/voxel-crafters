from src.classes.Block import Block
from src.assets.textures import TextureSets
from src.assets.materials import Materials
from src.classes.shapes import Cube

class Grass(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, TextureSets.grass, Materials.grass, Cube(), 100)