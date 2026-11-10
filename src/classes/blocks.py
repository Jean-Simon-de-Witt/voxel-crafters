from src.classes.Block import Block
from src.assets.textures import TextureSets
from src.assets.materials import Materials
from src.classes.shapes import Cube

class Grass(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.grass, Materials.grass, Cube(), 100)
        
class Stone(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.stone, Materials.stone, Cube(), 200)

class CoalOre(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.coal_ore, Materials.stone, Cube(), 250)

class IronOre(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.iron_ore, Materials.stone, Cube(), 300)

class GoldOre(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.gold_ore, Materials.stone, Cube(), 275)
        
class DiamondOre(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.diamond_ore, Materials.stone, Cube(), 400)

class Wood(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.wood, Materials.wood, Cube(), 150)
        
class Leaves(Block):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0, 1.0, 1.0, TextureSets.leaves, Materials.leaves, Cube(), 50)