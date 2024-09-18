from graphics2.model import Cube
import glm

class Scene:
    def __init__(self, app):
        self.app = app
        self.cubes = []
        self.load()
        
    def load(self):
        app = self.app
        cube_position = glm.vec3(0.0, 0.0, 0.0)
        self.cubes.append(Cube(app, position=cube_position))
        
    def update(self):
        for cube in self.cubes:
            cube.update()
           
    def render(self):
        for cube in self.cubes:
            cube.render()