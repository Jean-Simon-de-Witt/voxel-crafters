from src.classes.Material import Material
from src.assets.audio import SoundEffects

class Materials:
    grass: Material = Material("solid", SoundEffects.grass_place, SoundEffects.grass_break, SoundEffects.grass_walk_on)
    stone: Material = Material("solid", SoundEffects.stone_place, SoundEffects.stone_break, SoundEffects.stone_walk_on)
    wood: Material = Material("solid", SoundEffects.wood_place, SoundEffects.wood_break, SoundEffects.wood_walk_on)
    leaves: Material = Material("solid", SoundEffects.leaves_place, SoundEffects.leaves_break, SoundEffects.leaves_walk_on)