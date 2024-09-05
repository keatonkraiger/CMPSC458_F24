class VAO:
    """
    Vertex Array Object (VAO) for managing vertex attribute configuration.
    
    VAOs store all the state needed to supply vertex data to the GPU.
    """ 
    def __init__(self, context, program, vbo):
        """
        Creates a VAO and sets up attribute pointers for position and color data.
        
        Args:
            context (moderngl.Context): The ModernGL context
            program (moderngl.Program): The shader program to use
            vbo (VBO): The Vertex Buffer Object containing vertex data
        """
        self.vao = context.vertex_array(
            program,
            [
                (vbo.vbo, '3f 3f', 'in_position', 'in_color'), # Format: 3 floats for position, 3 floats for color
            ]
        )
    
    def render(self):
        """Renders the VAO, drawing the triangle to the screen."""
        self.vao.render()

    def destroy(self):
        # Release the VAO to free up GPU resources
        self.vao.release()