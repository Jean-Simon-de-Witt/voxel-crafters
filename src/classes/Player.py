import pygame
import math
from src.classes.Collider import Collider

class Player:
    def __init__(self, x: float, y: float, z: float, speed: int, jump_height: int, health: float = 100, hunger: float = 100):
        self._x: float = x
        self._y: float = y
        self._z: float = z
        
        self._collider = Collider(x, y, z, 0.8, 1.8, 0.8)
        
        self._pitch: float = 0.0
        self._yaw: float = 0.0
        self._mouse_sensitivity: float = 0.2
        
        self._speed: int = speed
        self._jump_height: int = jump_height
        self._reach: float = 5.0
        
        self._gravity: float = 15.0
        self._is_on_ground: bool = False
        
        self._change_x: float = 0
        self._change_y: float = 0
        self._change_z: float = 0
        
        self._health: float = health
        self._hunger: float = hunger
        
        self._eye_height = 1.62
    
    def _raycast(self, world):
        yaw_rad = math.radians(self._yaw)
        pitch_rad = math.radians(self._pitch)
        
        dx = math.sin(yaw_rad) * math.cos(pitch_rad)
        dy = -math.sin(pitch_rad)
        dz = -math.cos(yaw_rad) * math.cos(pitch_rad)
        
        ray_x, ray_y, ray_z = self._x + 0.5, self._y + self._eye_height, self._z + 0.5
        grid_x, grid_y, grid_z = math.floor(ray_x), math.floor(ray_y), math.floor(ray_z)
        
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        step_z = 1 if dz > 0 else -1
        
        t_delta_x = abs(1.0 / dx) if dx != 0 else 1e30
        t_delta_y = abs(1.0 / dy) if dy != 0 else 1e30
        t_delta_z = abs(1.0 / dz) if dz != 0 else 1e30
        
        t_max_x = (grid_x + 1.0 - ray_x) * t_delta_x if dx > 0 else (ray_x - grid_x) * t_delta_x
        t_max_y = (grid_y + 1.0 - ray_y) * t_delta_y if dy > 0 else (ray_y - grid_y) * t_delta_y
        t_max_z = (grid_z + 1.0 - ray_z) * t_delta_z if dz > 0 else (ray_z - grid_z) * t_delta_z
        
        distance = 0.0
        hit_normal = (0, 0, 0)
        
        while distance < self._reach:
            if t_max_x < t_max_y and t_max_x < t_max_z:
                t_max_x += t_delta_x
                grid_x += step_x
                distance = t_max_x - t_delta_x
                hit_normal = (-step_x, 0, 0)
            elif t_max_y < t_max_z:
                t_max_y += t_delta_y
                grid_y += step_y
                distance = t_max_y - t_delta_y
                hit_normal = (0, -step_y, 0)
            else:
                t_max_z += t_delta_z
                grid_z += step_z
                distance = t_max_z - t_delta_z
                hit_normal = (0, 0, -step_z)
                
            target_block = world.get_block_at(grid_x, grid_y, grid_z)
            
            if target_block is not None:
                return target_block, hit_normal
            
        return None, None
    
    def _apply_gravity(self, time_passed_seconds: float) -> None:
        self._change_y -= self._gravity * time_passed_seconds
        
    def _move(self, time_passed_seconds: float, world) -> None:
        previous_y = self._y
        
        self._x += self._change_x * time_passed_seconds
        self._y += self._change_y * time_passed_seconds
        self._z += self._change_z * time_passed_seconds
        
        self._collider.update_position(self._x, self._y, self._z)
        
        self._is_on_ground = False
        
        min_x = math.floor(self._x - (self._collider.get_width() / 2) + 0.5)
        max_x = math.ceil(self._x + (self._collider.get_width() / 2) + 0.5)
        min_y = math.floor(self._y - (self._collider.get_height() / 2) - 0.1 + 0.5)
        max_y = math.ceil(self._y + (self._collider.get_height() / 2) + 0.5)
        min_z = math.floor(self._z - (self._collider.get_depth() / 2) + 0.5)
        max_z = math.ceil(self._z + (self._collider.get_depth() / 2) + 0.5)
        
        for grid_x in range(min_x, max_x + 1):
            for grid_y in range(min_y, max_y + 1):
                for grid_z in range(min_z, max_z + 1):
                    block = world.get_block_at(grid_x, grid_y, grid_z)
                    
                    if block is not None:
                        if self._collider.intersects(block.get_collider()):
                            if self._change_y < 0:
                                self._y = block.get_y() + (block.get_height() /2) + (self._collider.get_height() / 2)
                                self._change_y = 0
                                self._is_on_ground = True
                                break
                
        self._collider.update_position(self._x, self._y, self._z)
    
    def _update_survival_stats(self, time_passed_seconds: float):
        
        hunger_depletion_rate = 0.5
        self._hunger -= hunger_depletion_rate * time_passed_seconds
        
        if self._hunger <= 0:
            self._hunger = 0
            health_depletion_rate = 1.0
            self._health -= health_depletion_rate * time_passed_seconds
    
    def _handle_mouse(self) -> None:
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        
        self._yaw += mouse_dx * self._mouse_sensitivity
        self._pitch += mouse_dy * self._mouse_sensitivity
        
        if self._pitch > 90.0:
            self._pitch = 90.0
        elif self._pitch < -90.0:
            self._pitch = -90.0
            
        self._yaw = self._yaw % 360.0
        
    def handle_mouse_clicks(self, event, world):
        if event.button == 1 or event.button == 3:
            
            target_block, hit_normal = self._raycast(world)
            
            if target_block is not None:
                if event.button == 1:
                    world.remove_block(target_block)
                elif event.button == 3:
                    place_x = target_block.get_x() + hit_normal[0]
                    place_y = target_block.get_y() + hit_normal[1]
                    place_z = target_block.get_z() + hit_normal[2]
                    from src.classes.Collider import Collider
                    temp_block_collider = Collider(place_x, place_y, place_z, 1.0, 1.0, 1.0)
                    
                    if not self._collider.intersects(temp_block_collider):
                        from src.classes.blocks import Grass
                        new_block = Grass(place_x, place_y, place_z)
                        world.add_block(new_block)
     
    def _handle_inputs(self) -> None:
        keys = pygame.key.get_pressed()
        
        self._change_x = 0
        self._change_z = 0
        
        yaw_rad = math.radians(self._yaw)
        
        forward_x = math.sin(yaw_rad)
        forward_z = -math.cos(yaw_rad)
        
        right_x = math.sin(yaw_rad + math.pi / 2)
        right_z = -math.cos(yaw_rad + math.pi / 2)
        
        if keys[pygame.K_w]:
            self._change_x += forward_x * self._speed
            self._change_z += forward_z * self._speed
        
        if keys[pygame.K_s]:
            self._change_x -= forward_x * self._speed
            self._change_z -= forward_z * self._speed
            
        if keys[pygame.K_a]:
            self._change_x -= right_x * self._speed
            self._change_z -= right_z * self._speed
            
        if keys[pygame.K_d]:
            self._change_x += right_x * self._speed
            self._change_z += right_z * self._speed
            
        if keys[pygame.K_SPACE] and self._is_on_ground:
            self._change_y = self._jump_height
            
    def update(self, delta_time_ms: int, world) -> None:
        time_passed_seconds = delta_time_ms / 1000.0
        
        if time_passed_seconds > 0.05:
            time_passed_seconds = 0.05
        self._handle_mouse()
        self._handle_inputs()
        
        self._apply_gravity(time_passed_seconds)
        self._move(time_passed_seconds, world)
        self._update_survival_stats(time_passed_seconds)
        
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
    
    def get_rotation(self) -> dict[str, float]:
        return {"pitch": self._pitch, "yaw": self._yaw}
    
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
    
    def get_eye_height(self) -> float:
        return self._eye_height