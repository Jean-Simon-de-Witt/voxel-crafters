from src.classes.Material import Material
from src.assets.audio import SoundEffects

class Materials:
    grass: Material = Material("solid", SoundEffects.grass_breaking, SoundEffects.grass_break, SoundEffects.grass_walk_on)