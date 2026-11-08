from src.classes.Texture import Texture
from src.classes.TextureSet import TextureSet

class Textures:
    grass_top: Texture =  Texture("src\\assets\\textures\\dirt_pack\\grasstop.png")
    grass_side: Texture = Texture("src\\assets\\textures\\dirt_pack\\grass.png")
    grass_bottom: Texture = Texture("src\\assets\\textures\\dirt_pack\\dirt.png")
    
class TextureSets:
    grass: TextureSet = TextureSet(Textures.grass_top, Textures.grass_side, Textures.grass_bottom)