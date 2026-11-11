class Collider:
    def __init__(self, x: float, y: float, z: float, width: float, height: float, depth: float):
        self._x: float = x
        self._y: float = y
        self._z: float = z
        self._width: float = width
        self._height: float = height
        self._depth: float = depth
        
    def update_position(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z
        
    def intersects(self, other: Collider) -> bool:
        min_x1 = self._x
        max_x1 = self._x + self._width
        min_y1 = self._y
        max_y1 = self._y + self._height
        min_z1 = self._z
        max_z1 = self._z + self._depth
        
        min_x2 = other.get_x()
        max_x2 = other.get_x() + other.get_width()
        min_y2 = other.get_y()
        max_y2 = other.get_y() + other.get_height()
        min_z2 = other.get_z()
        max_z2 = other.get_z() + (other.get_depth() / 2)
        
        overlap_x = min_x1 <= max_x2 and max_x1 >= min_x2
        overlap_y = min_y1 <= max_y2 and max_y1 >= min_y2
        overlap_z = min_z1 <= max_z2 and max_z1 >= min_z2
        
        return overlap_x and overlap_y and overlap_z
        
    def get_x(self) -> float:
        return self._x
    
    def get_y(self) -> float:
        return self._y
    
    def get_z(self) -> float:
        return self._z
    
    def get_width(self) -> float:
        return self._width
    
    def get_height(self) -> float:
        return self._height
    
    def get_depth(self) -> float:
        return self._depth