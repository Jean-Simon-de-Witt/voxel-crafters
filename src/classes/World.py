import random
from src.classes.Block import Block
from src.classes.blocks import Grass, Stone
from src.classes.structures import Tree, CoalVein

class World:
    def __init__(self, size_x: int, size_z: int, depth: int):
        self._size_x: int = size_x
        self._size_z: int = size_z
        self._depth: int = depth
        self._blocks: list[Block] = []
        
        self._generate_layered_world()
    
    def _generate_layered_world(self):
        for x in range(self._size_x):
            for z in range(self._size_z):
                world_x = x - (self._size_x / 2)
                world_z = z - (self._size_z / 2)
                
                self._blocks.append(Grass(world_x, 0, world_z))
                
                if random.random() < 0.05:
                    tree_blocks = Tree.generate(world_x, 1, world_z)
                    self._blocks.extend(tree_blocks)
                    
                for y in range(1, self._depth + 1):
                    world_y = -y
                    
                    if random.random() < 0.02:
                        vein_blocks = CoalVein.generate(world_x, world_y, world_z)
                        self._blocks.extend(vein_blocks)
       
    def _generate_flat_world(self):
        for x in range(self._size_x):
            for z in range(self._size_z):
                world_x = x - (self._size_x / 2)
                world_z = z - (self._size_z / 2)
                
                new_block = Grass(world_x, 0, world_z)
                
                self._blocks.append(new_block)
                
    def draw(self):
        for block in self._blocks:
            block.draw()
            
    def get_blocks(self) -> list[Block]:
        return self._blocks
    