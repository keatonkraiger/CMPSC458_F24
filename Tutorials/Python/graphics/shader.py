
class Shader:
    """
    Manages the compilation and usage of OpenGL shader programs. This class is responsible for loading vertex and fragment 
    shaders from files, compiling them into a shader program, and providing access to that program.
   
    Args:
        context (moderngl.Context): The ModernGL context to use for shader compilation. 
    """ 
    def __init__(self, context):
        self.context = context
        self.programs = {}
        self.programs['default'] = self.get_program(shader_name='default')
    
    def get_program(self, shader_name='default', shader_path='Media/Shaders'):
        """  Load and compile a shader program from a vertex and fragment shader file.
        
        Args:
            shader_name (str, optional):  Name of the shader files (without extension). Defaults to 'default'.
            shader_path (str, optional): Path to the directory containing shader files. Defaults to 'Media/Shaders'.

        Returns:
            moderngl.Program: Compiled shader program
        """
        with open(f'{shader_path}/{shader_name}.vert', 'r') as file:
            vertex_shader = file.read()
            
        with open(f'{shader_path}/{shader_name}.frag', 'r') as file:
            fragment_shader = file.read()
       
        program = self.context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        """Releases the shader program to free up GPU resources."""
        self.programs['default'].release()
