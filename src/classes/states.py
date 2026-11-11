import pygame
from pygame.locals import *
from OpenGL.GL import *
from src.classes.GameState import GameState
from src.classes.ui import Label, Button, Hotbar

def setup_2d_projection(display_size):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display_size[0], display_size[1], 0, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
def restore_3d_projection():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

class MainMenuState(GameState):
    def __init__(self, engine):
        super().__init__(engine)
        self._font_title = pygame.font.SysFont("Arial", 64, bold=True)
        self._font_btn = pygame.font.SysFont("Arial", 32)
        
        cx = engine.display_size[0] // 2
        cy = engine.display_size[1] // 2
        
        self._title = Label(cx - 200, cy + 100, "Voxel Crafters", self._font_title)
        
        self._btn_play: Button = Button(cx - 100, cy, 200, 60, "Play", self._font_btn, self.start_game)
        self._btn_quit: Button = Button(cx - 100, cy - 100, 200, 60, "Quit", self._font_btn, self.quit_game)
        
    def start_game(self):
        self.engine.change_state(PlayState(self.engine))
        
    def quit_game(self):
        self.engine.running = False
        
    def handle_events(self, events):
        for event in events:
            self._btn_play.handle_event(event)
            self._btn_quit.handle_event(event)
            
    def update(self, delta_time):
        pass
    
    def draw(self, display_size):
        glClearColor(0.1, 0.2, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        setup_2d_projection(display_size)
        
        self._title.draw()
        self._btn_play.draw()
        self._btn_quit.draw()
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        restore_3d_projection()
        
    def get_play_button(self) -> Button:
        return self._btn_play
    
    def get_quite_button(self) -> Button:
        return self._btn_quit
    
class PauseState(GameState):
    def __init__(self, engine, play_state: PlayState):
        super().__init__(engine)
        self._play_state: PlayState = play_state
        self._font = pygame.font.SysFont("Arial", 48, bold = True)
            
        cx = engine.display_size[0] // 2
        cy = engine.display_size[1] // 2
        self._label: Label = Label(cx - 100, cy + 100, "PAUSED", self._font)
        self._btn_resume: Button = Button(cx - 150, cy, 300, 60, "Resume Game", pygame.font.SysFont("Arial", 32), self.resume)
        self._btn_menu = Button(cx - 150, cy - 100, 300, 60, "Exit to Menu", pygame.font.SysFont("Arial", 32), self.exit_to_menu)
            
    def resume(self):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.engine.change_state(self._play_state)
            
    def exit_to_menu(self):
        self.engine.change_state(MainMenuState(self.engine))
            
    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.resume()
            self._btn_resume.handle_event(event)
            self._btn_menu.handle_event(event)
                
    def update(self, delta_time):
        pass
        
    def draw(self, display_size):
        self._play_state.draw(display_size, draw_ui = False)
            
        setup_2d_projection(display_size)
        self._label.draw()
        self._btn_resume.draw()
        self._btn_menu.draw()
        restore_3d_projection()
            
    def get_saved_play_state(self) -> PlayState:
        return self._play_state
        
    def get_label(self) -> Label:
        return self._label
        
    def get_resume_button(self) -> Button:
        return self._btn_resume
        
    def get_menu_button(self) -> Button:
        return self._btn_menu
        
class PlayState(GameState):
    def __init__(self, engine):
        super().__init__(engine)
        
        from src.classes.World import World
        from src.classes.Player import Player
        
        self.world: World = World(20, 20, 3)
        self.player: Player = Player(0, 2, 0, speed = 10, jump_height = 5)
        
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self._ui_font = pygame.font.SysFont("Arial", 24, bold = True)
        self._hotbar: Hotbar = Hotbar(20, 20, self.player, self._ui_font) 
        
    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.event.set_grab(False)
                pygame.mouse.set_visible(True)
                self.engine.change_state(PauseState(self.engine, self))
                
            if event.type == MOUSEBUTTONDOWN:
                self.player.handle_mouse_clicks(event, self.world)
                
    def update(self, delta_time):
        self.player.update(delta_time, self.world)
        
    def draw(self, display_size, draw_ui = True):
        glClearColor(0.5, 0.8, 1.0, 1.0)
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
        
        if draw_ui:
            setup_2d_projection(display_size)
            cx, cy = display_size[0] // 2, display_size[1] // 2
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_LINES)
            glVertex2f(cx, cy - 10); glVertex2f(cx, cy + 10)
            glEnd()
            
            self._hotbar.draw()
            restore_3d_projection()