from src.classes.Texture import Texture
class TextureSet:
    def __init__(self, texture_top: Texture, texture_side: Texture, texture_bottom: Texture):
        self._texture_top: Texture = texture_top
        self._texture_side: Texture = texture_side
        self._texture_bottom: Texture = texture_bottom
        
    def set_top(self, texture_top: Texture) -> None:
        self._texture_top = texture_top
    
    def set_side(self, texture_side: Texture) -> None:
        self._texture_side = texture_side
        
    def set_bottom(self, texture_bottom: Texture) -> None:
        self._texture_bottom = texture_bottom
        
    def set_textures(self, texture_top: Texture, texture_side: Texture, texture_bottom: Texture) -> None:
        self._texture_top = texture_top
        self._texture_side = texture_side
        self._texture_bottom = texture_bottom
        
    def get_top(self) -> Texture:
        return self._texture_top
    
    def get_side(self) -> Texture:
        return self._texture_side
    
    def get_bottom(self) -> Texture:
        return self._texture_bottom
    
    def get_textures(self) -> dict[str, Texture]:
        return {"top": self._texture_top, "side": self._texture_side, "bottom": self._texture_bottom}
    
