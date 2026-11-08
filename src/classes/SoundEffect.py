import pygame

class SoundEffect:
    def __init__(self, audio_file_path: str):
        self._audio_path: str = audio_file_path
        self._sound_object: pygame.mixer.Sound = pygame.mixer.Sound(audio_file_path)
    
    def set_audio(self, audio_file_path: str) -> None:
        self._audio_path = audio_file_path
        self._sound_object = pygame.mixer.Sound(audio_file_path)
        
    def play(self) -> None:
        self._sound_object.play()
        
    def stop(self) -> None:
        self._sound_object.stop()