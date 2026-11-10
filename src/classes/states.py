import pygame
from pygame.locals import *
from OpenGL.GL import *
from src.classes.GameState import GameState

class PlayState(GameState):
    def __init__(self, engine):
        super().__init__(engine)
        
        from src.classes.World import World
        from src.classes.Player import Player
        
        self.world: World = World(20, 20, 3)
        self.player: Player = Player(0, 1, 0, speed = 10, jump_height = 5)
        
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        
        glClearColor(0.5, 0.8, 1.0, 1.0)
        
    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.event.set_grab(False)
                pygame.mouse.set_visible(True)
                self.engine.change_state(MainMenuState(self.engine))
                
            if event.type == MOUSEBUTTONDOWN:
                self.player.handle_mouse_clicks(event, self.world)
                
    def update(self, delta_time):
        self.player.update(delta_time, self.world)
        
    def draw(self, display_size):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        rot = self.player.get_rotation()
        glRotatef(rot['pitch'], 1, 0, 0)
        glRotatef(rot['yaw'], 0, 1, 0)
        
        pos = self.player.get_position()
        camera_y = pos['y'] + self.player.get_eye_height()
        glTranslatef(-pos['x'], -camera_y, -pos['z'])
        
        self.world.draw()

class MainMenuState(GameState):
    def __init__(self, engine):
        super().__init__(engine)
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 48, bold = True)
        
    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.engine.change_state(PlayState(self.engine))
                elif event.key == K_ESCAPE:
                    self.engine.running = False
                    
    def update(self, delta_time):
        pass
    
    def draw(self, display_size):
        glClearColor(0.1, 0.2, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, display_size[0], display_size[1], 0, -1, 1)
        
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        text_surface = self.font.render("Voxel Crafters - Press Enter to Play", True, (255, 255, 255))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        
        text_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_surface.get_width(), text_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        
        cx = (display_size[0] - text_surface.get_width()) // 2
        cy = (display_size[1] - text_surface.get_height()) // 2
        w, h = text_surface.get_width(), text_surface.get_height()
        
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(cx, cy)
        glTexCoord2f(1, 0); glVertex2f(cx + w, cy)
        glTexCoord2f(1, 1); glVertex2f(cx + w, cy - h)
        glTexCoord2f(0, 1); glVertex2f(cx, cy - h)
        glEnd()
        
        glDeleteTextures(1, [text_id])
        glDisable(GL_BLEND)
        
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()