import random
from src.classes.Block import Block
from src.classes.blocks import Wood, Leaves, CoalOre

class Tree:
    @staticmethod
    def generate(x: float, y: float, z: float) -> list[Block]:
        blocks = []
        
        height = random.randint(3, 5)
        
        for i in range(height):
            blocks.append(Wood(x, y + i, z))
            
        leaf_y = y + height
        blocks.append(Leaves(x, leaf_y, z))
        blocks.append(Leaves(x + 1, leaf_y - 1, z))
        blocks.append(Leaves(x - 1, leaf_y - 1, z))
        blocks.append(Leaves(x, leaf_y -1, z + 1))
        blocks.append(Leaves(x, leaf_y - 1, z - 1))
        return blocks
        
class CoalVein:
    @staticmethod
    def generate(x: float, y: float, z: float) -> list[Block]:
        blocks = []
        size = random.randint(1, 3)
        
        blocks.append(CoalOre(x, y, z))
        if size > 1:
            blocks.append(CoalOre(x + 1, y, z))
        if size > 2:
            blocks.append(CoalOre(x, y - 1, z))
        return blocks