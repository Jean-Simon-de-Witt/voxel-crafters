import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init_opengl(display_size):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    
def load_assets():
    from src.classes.World import World
    from src.classes.Player import Player
    
    return {"world": World(20, 20), "player": Player(0, 2, 5, speed = 10, jump_height = 5)}
    
def main():
    pygame.init()
    pygame.mixer.init()
    
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_opengl(display)
    
    assets = load_assets()
    
    flat_world = assets.get("world")
    player = assets.get("player")
    
    clock = pygame.time.Clock()
    running = True
    while running:
        delta_time = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        player.update(delta_time)
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        pos = player.get_position()
        gluLookAt(pos['x'], pos['y'], pos['z'], pos['x'], pos['y'], pos['z'] - 1, 0, 1, 0)
        
        flat_world.draw()
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()