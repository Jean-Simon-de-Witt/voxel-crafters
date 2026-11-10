import random
import math
from src.classes.Block import Block
from src.classes.blocks import Grass, Stone
from src.classes.structures import Tree, CoalVein

class World:
    def __init__(self, size_x: int, size_z: int, depth: int):
        self._size_x: int = size_x
        self._size_z: int = size_z
        self._depth: int = depth
        self._blocks: dict[tuple, Block] = {}
        
        self._generate_layered_world()
        self.update_all_blocks_visibility()
        
    def update_all_blocks_visibility(self) -> None:
        for block in self.get_blocks():
            block.update_visibility(self)
    
    def _add_block(self, block: Block) -> None:
        pos_key = (int(math.floor(block.get_x())), int(math.floor(block.get_y())), int(math.floor(block.get_z())))
        self._blocks[pos_key] = block  
    
    def _generate_layered_world(self):
        for x in range(self._size_x):
            for z in range(self._size_z):
                world_x = x - (self._size_x / 2)
                world_z = z - (self._size_z / 2)
                
                self._add_block(Grass(world_x, 0, world_z))
            
                if random.random() < 0.05:
                    tree_blocks = Tree.generate(world_x, 1, world_z)
                    for b in tree_blocks:
                        self._add_block(b)
                    
                for y in range(1, self._depth + 1):
                    world_y = -y
                    if random.random() < 0.02:
                        vein_blocks = CoalVein.generate(world_x, world_y, world_z)
                        for b in vein_blocks:
                            self._add_block(b)
                    else:
                        self._add_block(Stone(world_x, world_y, world_z))
       
    def _generate_flat_world(self):
        for x in range(self._size_x):
            for z in range(self._size_z):
                world_x = x - (self._size_x / 2)
                world_z = z - (self._size_z / 2)
                
                new_block = Grass(world_x, 0, world_z)
                
                self._blocks.append(new_block)
            
    def get_blocks(self) -> list[Block]:
        return list(self._blocks.values())
    
    def get_block_at(self, x: int, y: int, z: int) -> Block:
        return self._blocks.get((x, y, z), None)
    
    def draw(self):
        for block in self.get_blocks():
            block.draw()
            
    def add_block(self, block: Block) -> None:
        x, y, z = int(math.floor(block.get_x())), int(math.floor(block.get_y())), int(math.floor(block.get_z()))
        
        self._blocks[(x, y, z)] = block
        
        self._update_local_visibility(x, y, z)
        
    def remove_block(self, block: Block) -> None:
        x, y, z = int(math.floor(block.get_x())), int(math.floor(block.get_y())), int(math.floor(block.get_z()))
        
        self._blocks.pop((x, y, z), None)
        
        self._update_local_visibility(x, y, z)
        
    def _update_local_visibility(self, x: int, y: int, z: int):
        coords_to_check = [(x, y, z), (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        
        for cx, cy, cz in coords_to_check:
            neighbor = self.get_block_at(cx, cy, cz)
            if neighbor is not None:
                neighbor.update_visibility(self)
    