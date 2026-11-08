import pygame;

class Texture:
    def __init__(self, path: str):
        self._texture = pygame.image.load(path).convert_alpha()

    def get_texture(self):
        return self._texture
    
    def set_texture(self, path: str):
        self._texture = pygame.image.load(path).convert_alpha()