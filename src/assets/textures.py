from src.classes.Texture import Texture
from src.classes.TextureSet import TextureSet

class Textures:
    grass_top: Texture =  Texture("src\\assets\\textures\\dirt_pack\\grasstop.png")
    grass_side: Texture = Texture("src\\assets\\textures\\dirt_pack\\grass.png")
    grass_bottom: Texture = Texture("src\\assets\\textures\\dirt_pack\\dirt.png")
    stone: Texture = Texture("src\\assets\\textures\\Almost MC Texture Pack 1.3\\default\\textures\\default_stone.png")
    coal_ore: Texture = Texture("src\\assets\\textures\\edited\\coal_ore.png")
    iron_ore: Texture = Texture("src\\assets\\textures\\edited\\iron_ore.png")
    gold_ore: Texture = Texture("src\\assets\\textures\\edited\\gold_ore.png")
    diamond_ore: Texture = Texture("src\\assets\\textures\\edited\\diamond_ore.png")
    wood_top_bottom: Texture = Texture("src\\assets\\textures\\Almost MC Texture Pack 1.3\\default\\textures\\default_tree_top.png")
    wood_side: Texture = Texture("src\\assets\\textures\\Almost MC Texture Pack 1.3\\default\\textures\\default_tree.png")
    leaves: Texture = Texture("src\\assets\\textures\\Almost MC Texture Pack 1.3\\default\\textures\\default_leaves.png")
    
    
class TextureSets:
    grass: TextureSet = TextureSet(Textures.grass_top, Textures.grass_side, Textures.grass_bottom)
    stone: TextureSet = TextureSet(Textures.stone, Textures.stone, Textures.stone)
    coal_ore: TextureSet = TextureSet(Textures.coal_ore, Textures.coal_ore, Textures.coal_ore)
    iron_ore: TextureSet = TextureSet(Textures.iron_ore, Textures.iron_ore, Textures.iron_ore)
    gold_ore: TextureSet = TextureSet(Textures.gold_ore, Textures.gold_ore, Textures.gold_ore)
    diamond_ore: TextureSet = TextureSet(Textures.diamond_ore, Textures.diamond_ore, Textures.diamond_ore)
    wood: TextureSet = TextureSet(Textures.wood_top_bottom, Textures.wood_side, Textures.wood_top_bottom)
    leaves: TextureSet = TextureSet(Textures.leaves, Textures.leaves, Textures.leaves)