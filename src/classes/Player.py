import pygame

class Player:
    def __init__(self, x: float, y: float, z: float, speed: int, jump_height: int, health: float = 100, hunger: float = 100):
        self._x: float = x
        self._y: float = y
        self._z: float = z
        self._speed: int = speed
        self._jump_height: int = jump_height
        
        self._change_x: float = 0
        self._change_y: float = 0
        self._change_z: float = 0
        
        self._health: float = health
        self._hunger: float = hunger
        
    def set_x(self, x: float) -> None:
        self._x = x
        
    def set_y(self, y: float) -> None:
        self._y = y
        
    def set_z(self, z: float) -> None:
        self._z = z
        
    def set_position(self, x: float = None, y: float = None, z: float = None) -> None:
        self._x = x if x is not None else self._x
        self._y = y if y is not None else self._y
        self._z = z if z is not None else self._z
        
    def set_speed(self, speed: int) -> None:
        self._speed = speed
        
    def set_jump_height(self, jump_height: int) -> None:
        self.jump_height = jump_height
        
    def set_change_x(self, change_x: float) -> None:
        self._change_x = change_x 
    
    def set_change_y(self, change_y: float) -> None:
        self._change_y = change_y
        
    def set_change_z(self, change_z: float) -> None:
        self._change_z = change_z
        
    def set_change(self, change_x: float = None, change_y: float = None, change_z: float = None) -> None:
        self._change_x = change_x if change_x is not None else self._change_x
        self._change_y = change_y if change_y is not None else self._change_y
        self._change_z = change_z if change_z is not None else self._change_z
        
    def set_health(self, health: float) -> None:
        self._health = health
        
    def set_hunger(self, hunger: float) -> None:
        self._hunger = hunger
        
    def get_x(self) -> float:
        return self._x
    
    def get_y(self) -> float:
        return self._y
    
    def get_z(self) -> float:
        return self._z
    
    def get_position(self) -> dict[str, float]:
        return {"x": self._x, "y": self._y, "z": self._z}
    
    def get_speed(self) -> int:
        return self._speed
    
    def get_jump_height(self) -> int:
        return self._jump_height
    
    def get_change_x(self) -> float:
        return self._change_x
    
    def get_change_y(self) -> float:
        return self._change_y
    
    def get_change_z(self) -> float:
        return self._change_z
    
    def get_change(self) -> dict[str, float]:
        return {"change_x": self._change_x, "change_y": self._change_y, "change_z": self._change_z}
    
    def get_health(self) -> float:
        return self._health
    
    def get_hunger(self) -> float:
        return self._hunger
    
    def move(self) -> None:
        self._x += self._change_x
        self._y += self._change_y
        self._z += self._change_z
    
    def update_survival_stats(self, time_passed):
        
        hunger_depletion_rate = 0.5
        self._hunger -= hunger_depletion_rate * (time_passed / 1000.0)
        
        if self._hunger <= 0:
            self._hunger = 0
            health_depletion_rate = 1.0
            self._health -= health_depletion_rate * (time_passed / 1000.0)
      
    def handle_inputs(self) -> None:
        keys = pygame.keys.get_pressed()
        
        if keys[pygame.K_w]:
            self.set_change_x(self._speed)
        
        if keys[pygame.K_s]:
            self.set_change_x(-self._speed)
            
        if keys[pygame.K_a]:
            self.set_change_z(-self.speed)
            
        if keys[pygame.K_d]:
            self.set_change_z(self.speed)
            
    def update(self) -> None:
        self.handle_inputs()
        self.move()
        self.update_survival_stats()