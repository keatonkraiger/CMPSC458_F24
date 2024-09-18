import numpy as np

class VBO:
    """
    Vertex Buffer Object (VBO) for storing vertex data on the GPU.
    
    This class defines the geometry and color data for our triangle.
    """
    def __init__(self, context):  # where context is the ModernGL context
        self.vertices = np.array([
            # positions        # colors
            -0.5, -0.5, 0.0,   1.0, 0.0, 0.0,  # bottom left, 
             0.5, -0.5, 0.0,   0.0, 1.0, 0.0,  # bottom right, 
             0.0,  0.5, 0.0,   0.0, 0.0, 1.0,  # top, 
        ], dtype='f4') # 32-bit float
        self.vbo = context.buffer(self.vertices) # Create a buffer object

    def destroy(self):
        # Releases the VBO to free up GPU resources
        self.vbo.release()