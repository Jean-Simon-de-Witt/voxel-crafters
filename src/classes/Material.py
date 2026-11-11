from src.classes.SoundEffect import SoundEffect

class Material:
    def __init__(self, state: str, place_sound: SoundEffect, break_sound: SoundEffect, walk_sound: SoundEffect):
        self._state: str = "liquid" if state == "liquid" else "solid"
        self._place_sound: SoundEffect = place_sound
        self._break_sound: SoundEffect = break_sound
        self._walk_sound: SoundEffect = walk_sound
        
    def set_state(self, state: str) -> None:
        self._state = "liquid" if state == "liquid" else "solid"
        
    def set_place_sound(self, place_sound: SoundEffect) -> None:
        self._place_sound = place_sound
        
    def set_break_sound(self, break_sound: SoundEffect) -> None:
        self._break_sound = break_sound
        
    def set_walk_sound(self, walk_sound: SoundEffect) -> None:
        self._walk_sound = walk_sound
        
    def get_state(self) -> str:
        return self._state
    
    def get_place_sound(self) -> SoundEffect:
        return self._place_sound
    
    def get_break_sound(self) -> SoundEffect:
        return self._break_sound
    
    def get_walk_sound(self) -> SoundEffect:
        return self._walk_sound
        