import pygame
from OpenGL.GL import *

class UIElement:
    def __init__(self, x: float, y: float):
        self._x: float = x
        self._y: float = y
        
    def _render_surface_to_opengl(self, surface) -> None:
        text_data = pygame.image.tobytes(surface, "RGBA", True)
        width, height = surface.get_width(), surface.get_height()
        
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor3f(1.0, 1.0, 1.0)
        
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1); glVertex2f(self._x, self._y)
        glTexCoord2f(1, 1); glVertex2f(self._x + width, self._y)
        glTexCoord2f(1, 0); glVertex2f(self._x + width, self._y + height)
        glTexCoord2f(0, 0); glVertex2f(self._x, self._y + height)
        glEnd()
        
        glDeleteTextures(1, [texture_id])
        glDisable(GL_BLEND)
        
    def get_x(self) -> float:
        return self._x
    
    def get_y(self) -> float:
        return self._y
    
class Label(UIElement):
    def __init__(self, x: float, y: float, text: str, font, color: tuple[int] = (255, 255, 255)):
        super().__init__(x, y)
        self._text: str = text
        self._font = font
        self._color: tuple[int] = color
        
    def draw(self):
        surface = self._font.render(self._text, True, self._color)
        self._render_surface_to_opengl(surface)
        
    def set_text(self, text: str) -> None:
        self._text = text
        
    def set_font(self, font) -> None:
        self._font = font
        
    def set_color(self, R: int = None, G: int = None, B: int = None) -> None:
        r, g, b = self._color
        r = R if R is not None else r
        g = G if G is not None else g
        b = B if B is not None else b
        
        self._color = (r, g, b)
        
    def get_text(self) -> str:
        return self._text
    
    def get_font(self):
        return self._font
    
    def get_color(self) -> tuple[int]:
        return self._color
        
class Button(UIElement):
    def __init__(self, x: float, y: float, width: float, height: float, text: str, font, callback):
        super().__init__(x, y)
        self._width: float = width
        self._height: float = height
        self._text: str = text
        self._font = font
        self._callback = callback
        
        self._rect: pygame.Rect = pygame.Rect(x, y, width, height)
        
        self._color_normal: tuple[int] = (0, 200, 0)
        self._color_hover: tuple[int] = (0, 255, 0)
        self._text_color: tuple[int] = (255, 255, 255)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self._rect.collidepoint((mouse_x, mouse_y)):
                self._callback()
                
    def draw(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hover = self._rect.collidepoint((mouse_x, mouse_y))
        
        bg_color = self._color_hover if is_hover else self._color_normal
        
        surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
        surface.fill(bg_color)
        
        text_surf = self._font.render(self._text, True, self._text_color)
        text_rect = text_surf.get_rect(center = (self._width // 2, self._height // 2))
        surface.blit(text_surf, text_rect)
        
        self._render_surface_to_opengl(surface)
        
    def set_width(self, width: float) -> None:
        self._width = width
        
    def set_height(self, height: float) -> None:
        self._height = height
        
    def set_text(self, text: str) -> None:
        self._text = text
        
    def set_font(self, font) -> None:
        self._font = font
        
    def get_width(self) -> float:
        return self._width
    
    def get_height(self) -> float:
        return self._height
    
    def get_text(self) -> str:
        return self._text
    
    def get_font(self):
        return self._font
    
    def get_action(self):
        return self._callback
    
    def get_color_normal(self) -> tuple[int]:
        return self._color_normal
    
    def get_color_hover(self) -> tuple[int]:
        return self._color_hover
    
    def get_text_color(self) -> tuple[int]:
        return self._text_color
    
class Hotbar(UIElement):
    def __init__(self, x: float, y: float, player, font):
        super().__init__(x, y)
        self._player = player
        self._font = font
            
    def draw(self):
        block_name = self._player.get_selected_block_name()
        surface = pygame.Surface((300, 60), pygame.SRCALPHA)
            
        surface.fill((0, 0, 0, 150))
            
        text_surf = self._font.render(f"Holding: {block_name}", True, (255, 255, 255))
        surface.blit(text_surf, (20, 15))
            
        self._render_surface_to_opengl(surface)
            