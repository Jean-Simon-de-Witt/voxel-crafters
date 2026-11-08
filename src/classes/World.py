from src.classes.Block import Block
from src.classes.blocks import Grass

class World:
    def __init__(self, size_x: int, size_z: int):
        self._size_x: int = size_x
        self._size_z: int = size_z
        self._blocks: list[Block] = []
        
        self._generate_flat_world()
        
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
    