from src.classes.SoundEffect import SoundEffect

class Material:
    def __init__(self, state: str, breaking_sound: SoundEffect, break_sound: SoundEffect, walk_sound: SoundEffect):
        self._state: str = "liquid" if state == "liquid" else "solid"
        self._breaking_sound: SoundEffect = breaking_sound
        self._break_sound: SoundEffect = break_sound
        self._walk_sound: SoundEffect = walk_sound
        
    def set_state(self, state: str) -> None:
        self._state = "liquid" if state == "liquid" else "solid"
        
    def set_breaking_sound(self, breaking_sound: SoundEffect) -> None:
        self._breaking_sound = breaking_sound
        
    def set_break_sound(self, break_sound: SoundEffect) -> None:
        self._break_sound = break_sound
        
    def set_walk_sound(self, walk_sound: SoundEffect) -> None:
        self._walk_sound = walk_sound
        
    def get_state(self) -> str:
        return self._state
    
    def get_breaking_sound(self) -> SoundEffect:
        return self._breaking_sound
    
    def get_break_sound(self) -> SoundEffect:
        return self._break_sound
    
    def get_walk_sound(self) -> SoundEffect:
        return self._walk_sound
        