import pygame as pg
import moderngl as mgl
import sys

from .vbo import VBO
from .vao import VAO
from .shader import Shader

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
        
        self.clock = pg.time.Clock() # Create a clock to control the frame rate
        self.shader = Shader(self.context) # Create a shader program, which will be used to render the VBO
        self.vbo = VBO(self.context) # Create a VBO, which will be rendered by the shader program
        self.vao = VAO(self.context, self.shader.programs['default'], self.vbo) # Create a VAO, which will be used to render the VBO
      
    def render(self):
        self.context.clear(0.2, 0.3, 0.3)  # Set the background color
        self.vao.render() # Render the VAO
        pg.display.flip() 
        
    def run(self):
        while True:
            self.check_events() # Check for events such as input or window close
            self.render()  # Render the scene
            self.clock.tick(60) # Limit the frame rate to 60 FPS
            
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