class VAO:
    """
    Manages Vertex Array Objects (VAOs) for different 3D objects in the application.
    """

    def __init__(self, app):
        """
        Initialize the VAO manager.

        Args:
            app: The main application object.
        """
        self.context = app.context
        self.vbo = app.vbo
        self.shader = app.shader 
        self.vaos = {}
        
        # Create VAO for cube
        self.vaos['cube'] = self.get_vao(
            program = self.shader.programs['cube'],
            vbo_name = 'cube'
        )

        
    def get_vao(self, program, vbo_name):
        """
        Create and return a Vertex Array Object.

        Args:
            program: The shader program to use with this VAO.
            vbo_name (str): The name of the Vertex Buffer Object to use.

        Returns:
            moderngl.VertexArray: The created VAO.
        """
        vbo = self.vbo.vbos[vbo_name]
        ebo = self.vbo.ebos[vbo_name]
        format = self.vbo.formats[vbo_name]
        attributes = self.vbo.attributes[vbo_name]
        
        vao = self.context.vertex_array(program, [(vbo, format, *attributes)], ebo)
        return vao
    
    def render(self, vao_name):
        """
        Render the specified VAO.

        Args:
            vao_name (str): The name of the VAO to render.
        """
        vao = self.vaos[vao_name]
        vao.render()
    
    def destroy(self):
        """
        Release all VAOs to free up GPU resources.
        """
        [vao.release() for vao in self.vaos.values()]