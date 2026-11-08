import pygame

class SoundEffect:
    def __init__(self, audio_file_path: str):
        self._audio: pygame.mixer.Sound = pygame.mixer.Sound("")
        
    def set_audio(self, audio_file_path: str) -> None:
        self._audio = pygame.mixer.Sound("")
        
    def get_audio(self) -> pygame.mixer.Sound:
        return self._audio