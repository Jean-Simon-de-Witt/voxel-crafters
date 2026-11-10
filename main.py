import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from src.classes.states import MainMenuState

class GameEngine:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.display_size = (1920, 1080)
        self.screen = pygame.display.set_mode(self.display_size, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Voxel Engine")
        
        self.init_opengl()
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.active_state = MainMenuState(self)
        
    def init_opengl(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.display_size[0] / self.display_size[1]), 0.1, 50.0)
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        
    def change_state(self, new_state):
        self.active_state = new_state
        
    def run(self):
        while self.running:
            delta_time = self.clock.tick(60)
            
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    self.running = False
                    
            if self.active_state:
                self.active_state.handle_events(events)
                self.active_state.update(delta_time)
                self.active_state.draw(self.display_size)
                
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    engine = GameEngine()
    engine.run()