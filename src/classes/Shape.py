class Shape:
    def __init__(self, vertices: tuple[tuple[float]], faces: tuple[tuple[int]], texture_coordinates: tuple[tuple[float]]):
        self._vertices: tuple[tuple[float]] = vertices
        self._faces: tuple[tuple[int]] = faces
        self._texture_coordinates: tuple[tuple[float]] = texture_coordinates
        
    def get_vertices(self) -> tuple[tuple[float]]:
        return self._vertices
    
    def get_faces(self) -> tuple[tuple[int]]:
        return self._faces
    
    def get_texture_coordinates(self) -> tuple[tuple[float]]:
        return self._texture_coordinates