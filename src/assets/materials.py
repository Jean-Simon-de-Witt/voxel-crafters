from src.classes.Material import Material
from src.assets.audio import sound_effects

class materials:
    Grass: Material = Material("solid", sound_effects.grass_breaking, sound_effects.grass_break, sound_effects.grass_walk_on)