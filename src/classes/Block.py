from src.classes.TextureSet import TextureSet
from src.classes.Material import Material

class Block:
    def __init__(self, x: float, y: float, z: float, textures: TextureSet, material: Material, durability: int):
        self._x: float = x
        self._y: float = y
        self._z: float = z
        
        self._texture: TextureSet = textures
        self._material: Material = material
        
        self._durability: int = durability
        
    def set_x(self, x: float) -> None:
        self._x = x
        
    def set_y(self, y: float) -> None:
        self._y = y
        
    def set_z(self, z: float) -> None:
        self._z = z
    
    def set_position(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z
        
    def set_textures(self, textures: TextureSet) -> None:
        self._textures = textures
        
    def set_material(self, material: Material) -> None:
        self._material = material
        
    def set_durability(self, durability: int) -> None:
        self._durability = durability
        
    def get_x(self) -> float:
        return self._x
    
    def get_y(self) -> float:
        return self._y
    
    def get_z(self) -> float:
        return self._z
    
    def get_textures(self) -> TextureSet:
        return self._textures
    
    def get_material(self) -> Material:
        return self._material
    
    def get_durability(self) -> int:
        return self._durability