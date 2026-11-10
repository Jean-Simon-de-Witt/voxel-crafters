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
    
    return {"world": World(20, 20, 3), "player": Player(0, 0, 0, speed = 10, jump_height = 5)}

def draw_crosshair(display_size):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    glOrtho(0, display_size[0], display_size[1], 0, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    cx, cy = display_size[0] // 2, display_size[1] // 2
    
    glDisable(GL_TEXTURE_2D)
    glColor3f(1.0, 1.0, 1.0)
    
    glBegin(GL_LINES)
    glVertex2f(cx - 10, cy)
    glVertex2f(cx + 10, cy)
    glVertex2f(cx, cy - 10)
    glVertex2f(cx, cy + 10)
    glEnd()
    
    glEnable(GL_TEXTURE_2D)
    glColor3f(1.0, 1.0, 1.0)
    
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
    
def main():
    pygame.init()
    pygame.mixer.init()
    
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_opengl(display)
    
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
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
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                player.handle_mouse_clicks(event, flat_world)
         
        player.update(delta_time, flat_world)
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        rot = player.get_rotation()
        glRotatef(rot['pitch'], 1, 0, 0)
        glRotatef(rot['yaw'], 0, 1, 0)
        
        pos = player.get_position()
        
        camera_y = pos['y'] + player.get_eye_height()
        glTranslate(-pos['x'], -camera_y, -pos['z'])
        
        flat_world.draw()
        draw_crosshair(display)
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()