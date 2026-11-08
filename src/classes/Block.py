from src.classes.TextureSet import TextureSet
from src.classes.Material import Material
from src.classes.Shape import Shape
from src.classes.Collider import Collider
from OpenGL.GL import *

class Block:
    def __init__(self, x: float, y: float, z: float, width: float, height: float, depth: float, textures: TextureSet, material: Material, shape: Shape, durability: int):
        self._x: float = x
        self._y: float = y
        self._z: float = z
        
        self._width: float = width
        self._height: float = height
        self._depth: float = depth
        
        self._collider: Collider = Collider(x, y, z, width, height, depth)
        self._textures: TextureSet = textures
        self._material: Material = material
        self._shape: Shape = shape
        
        self._durability: int = durability
        
        self._world_vertices = self._calculate_world_vertices()
        
    def _calculate_world_vertices(self) -> tuple:
        world_verts = []
        for vertex in self._shape.get_vertices():
            world_verts.append((vertex[0] + self._x, vertex[1] + self._y, vertex[2] + self._z))
        return tuple(world_verts)
    
    def draw(self) -> None:
        tex_coords = self._shape.get_texture_coordinates()
        
        for face_index, face in enumerate(self._shape.get_faces()):
            if face_index == 4:
                texture_id = self._textures.get_top().get_texture_id()
            elif face_index == 5:
                texture_id = self._textures.get_bottom().get_texture_id()
            else:
                texture_id = self._textures.get_side().get_texture_id()
                
            glBindTexture(GL_TEXTURE_2D, texture_id)
            
            glBegin(GL_QUADS)
            for i, vertex_index in enumerate(face):
                glTexCoord2fv(tex_coords[i])
                glVertex3fv(self._world_vertices[vertex_index])
            glEnd()
        
    def set_position(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z
        self._world_vertices = self._calculate_world_vertices()
        
        self._collider.update_position(x, y, z)
        
    def set_x(self, x: float) -> None:
        self._x = x
        
    def set_y(self, y: float) -> None:
        self._y = y
        
    def set_z(self, z: float) -> None:
        self._z = z
        
    def set_textures(self, textures: TextureSet) -> None:
        self._textures = textures
        
    def set_material(self, material: Material) -> None:
        self._material = material
        
    def set_shape(self, shape: Shape) -> None:
        self._shape = shape
        
    def set_durability(self, durability: int) -> None:
        self._durability = durability
        
    def get_x(self) -> float:
        return self._x
    
    def get_y(self) -> float:
        return self._y
    
    def get_z(self) -> float:
        return self._z
    
    def get_width(self) -> float:
        return self._width
    
    def get_height(self) -> float:
        return self._height
    
    def get_depth(self) -> float:
        return self._depth
    
    def get_dimensions(self) -> dict[str, float]:
        return {"width": self._width, "height": self._height, "depth": self._depth}
    
    def get_collider(self) -> Collider:
        return self._collider
    
    def get_textures(self) -> TextureSet:
        return self._textures
    
    def get_material(self) -> Material:
        return self._material
    
    def get_shape(self) -> Shape:
        return self._shape
    
    def get_durability(self) -> int:
        return self._durability