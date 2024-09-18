import pygame as pg
import moderngl as mgl
import numpy as np
import sys
import glm

from graphics2.camera import Camera 
from graphics2.vbo import VBO
from graphics2.vao import VAO
from graphics2.shader import Shader
from graphics2.scene import Scene
from graphics2.texture import Texture
from graphics2.shader import Shader


# Note that we are mostly sticking with the overall structure of the original code/the code from project 1.
class Engine:
    """
    Main engine class that manages the game loop and rendering process.
    
    This class initializes Pygame and ModernGL, creates necessary objects (VBO, VAO, Shader),
    and handles the main game loop including event processing and rendering.
    """
    def __init__(self, width=800, height=600):
        pg.init()
        self.window_size = (width, height)
       
        # Set OpenGL context attributes 
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) # OpenGL Major Version 3.0
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3) # OpenGL Minor Version 3.3
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) # Core Profile (No deprecated functions)
        pg.display.set_mode(self.window_size, flags=pg.OPENGL | pg.DOUBLEBUF) # Create an OpenGL window
        self.context = mgl.create_context() # Create a ModernGL context
        self.context.enable(flags=mgl.DEPTH_TEST)
       
        # Configure mouse settings
        pg.event.set_grab(True) 
        pg.mouse.set_visible(False) 
        
        self.clock = pg.time.Clock() # Create a clock to control the frame rate
        self.time = 0
        self.dt = 0
       
        self.camera = Camera(self) 
        self.shader = Shader(self.context) # Create a shader program, which will be used to render the VBO
        self.texture = Texture(self.context)
        self.vbo = VBO(self.context) # Create a VBO, which will be rendered by the shader program
        self.vao = VAO(self) # Create a VAO, which will be used to render the VBO
        self.scene = Scene(self)
       
        self.background_color = (0.2, 0.3, 0.3, 1.0)  # Add this line
 
        self.rotation = glm.vec3(glm.radians(90.0), 0.0, 0.0)
        self.demonstrate_transformations()
        

    def mat_to_string(self, mat):
        ''' 
        Convert a matrix to a string for display.
        '''
        rows = len(mat)
        cols = len(mat[0])
        result = f"mat{rows}x{cols}(\n"
        for i in range(rows):
            result += "  (" + ", ".join(format_number(v) for v in mat[i]) + ")"
            if i < rows - 1:
                result += ",\n"
        result += "\n)"
        return result

    def vec_to_string(self, vec):
        '''
        Pretty print a vector.
        '''
        return f"vec{len(vec)}({', '.join(format_number(v) for v in vec)})"


    def demonstrate_transformations(self):
        '''
        Show off some basic transformations and matrix operations using glm.
        '''
        print("Example of defining a matrix")
        mat = glm.mat3(1.0, 0.0, 0.0,
                       1.0, 0.0, 0.0,
                       0.0, 0.0, 1.0)
        print(self.mat_to_string(mat))
        print()

        # Example Translation, multiply, and subtract
        vec = glm.vec4(1.0, 0.0, 0.0, 1.0)
        trans = glm.mat4(1.0)
        trans = glm.translate(trans, glm.vec3(1.0, 1.0, 0.0))
        print(f"Before translation: {self.vec_to_string(vec)}")
        vec = trans * vec
        print(f"After translation: {self.vec_to_string(vec)}")
        vec -= glm.vec4(1.0, 1.0, 0.0, 0.0)
        print(f"After subtraction: {self.vec_to_string(vec)}")
        print()

        # Example of multiplying matrices
        print("Translation matrix:")
        print(self.mat_to_string(trans))
        trans = trans * trans
        print("Matrix squared:")
        print(self.mat_to_string(trans))
        print()

    def update(self):
        self.dt = self.clock.tick() / 1000.0
        self.time = pg.time.get_ticks() / 1000.0
        self.camera.update()
        self.scene.update()
        
        # Update rotation
        self.rotation.y = self.time
        self.rotation.z = self.time

    def render(self):
        self.context.clear(*self.background_color)
        self.scene.render()
        pg.display.flip()

    def run(self):
        while True:
            self.check_events() # Check for events such as input or window close
            self.update()
            self.render()  # Render the scene
            
    def check_events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): # If the window is closed or the escape key is pressed
                self.destroy()
                pg.quit()
                sys.exit()
       
    def destroy(self):
        # Destroy the VBO, VAO, and shader program
        self.vbo.destroy() 
        self.vao.destroy()
        self.shader.destroy()
        
    def mat_to_string(self, mat):
        ''' 
        Convert a matrix to a string for display.
        '''
        rows = len(mat)
        cols = len(mat[0])
        result = f"mat{rows}x{cols}(\n"
        for i in range(rows):
            result += "  (" + ", ".join(format_number(v) for v in mat[i]) + ")"
            if i < rows - 1:
                result += ",\n"
        result += "\n)"
        return result

    def vec_to_string(self, vec):
        '''
        Pretty print a vector.
        '''
        return f"vec{len(vec)}({', '.join(format_number(v) for v in vec)})"
        
def format_number(num):
    '''
        Quickie to format a number for display.
    '''
    if abs(num) < 1e-6:
        return "0"
    elif abs(num - round(num)) < 1e-6:
        return f"{int(round(num))}"
    else:
        return f"{num:.6f}".rstrip('0').rstrip('.')      