import pygame;
from OpenGL.GL import *

class Texture:
    def __init__(self, path: str):
        self._texture_surface = pygame.image.load(path).convert_alpha()
        self._texture_id = self._generate_gl_texture()
        
    def _generate_gl_texture(self) -> int:
        texture_data = pygame.image.tostring(self._texture_surface, "RGBA", 1)
        width, height = self._texture_surface.get_size()
        
        tex_id = glGenTextures(1)
        
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        
        return tex_id
    
    def get_texture_id(self) -> int:
        return self._texture_id
    