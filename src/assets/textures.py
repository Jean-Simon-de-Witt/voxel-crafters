from classes.Texture import Texture
from classes.TextureSet import TextureSet

class textures:
    grass_top: Texture =  Texture("")
    grass_side: Texture = Texture("")
    grass_bottom: Texture = Texture("")
    
class texture_sets:
    grass: TextureSet = TextureSet(textures.grass_top, textures.grass_side, textures.grass_bottom)