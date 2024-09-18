import numpy as np
import glm

class BaseModel:
    """
    Base class for 3D models in the application.
    """

    def __init__(self, app, vao_name, tex_id):
        """
        Initialize the BaseModel.

        Args:
            app: The main application object.
            vao_name (str): Name of the Vertex Array Object.
            tex_id (str): Identifier for the texture.
        """
        self.app = app
        self.vao_name = vao_name
        self.tex_id = tex_id
        self.m_model = self.get_model_matrix()
        self.program = app.shader.programs[vao_name]
        self.camera = app.camera
        self.texture = app.texture.textures[self.tex_id]
        
    def update(self):
        """
        Update the model's shader uniforms.
        """
        self.texture.use()
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def get_model_matrix(self):
        """
        Get the model matrix for the object.

        Returns:
            numpy.ndarray: A 4x4 identity matrix.
        """
        return np.eye(4, dtype='f4')
    
    def render(self):
        """
        Render the model.
        """
        self.update()
        self.app.vao.render(self.vao_name)
        
class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id='container', position=glm.vec3(0.0)):
        """
        Initialize the Cube object.
        
        :param app: The main application object
        :param vao_name: Name of the Vertex Array Object
        :param tex_id: ID of the texture to be used
        :param position: Initial position of the cube
        """
        super().__init__(app, vao_name, tex_id)
        self.position = position
        # Set up texture units
        self.program['texture1'] = 0
        self.program['texture2'] = 1
        # Set the projection matrix in the shader
        self.program['m_proj'].write(self.camera.m_projection)
        # Load the second texture
        self.texture2 = app.texture.textures['awesomeface']
        # Flag to control first update behavior
        self.first_update = True

    def update(self):
        """
        Update the cube's state and apply transformations.
        This method is called every frame.
        """
        # Bind textures to their respective texture units
        self.texture.use(location=0)
        self.texture2.use(location=1)
        
        # Update view and projection matrices in the shader
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_proj'].write(self.camera.m_projection)
        
        # Start with identity matrix
        model = glm.mat4(1.0)
        if self.first_update:
            print("Model matrix initialization:")
            print(self.app.mat_to_string(model))
            print()

        # Apply translation
        model = glm.translate(model, glm.vec3(0.0, 0.0, -1.0))
        if self.first_update:
            print("Model matrix after translation of -1 in z dimension:")
            print(self.app.mat_to_string(model))
            print()

        # Apply rotation
        model = glm.rotate(model, self.app.rotation.x, glm.vec3(1, 0, 0))  # Rotate around x-axis
        model = glm.rotate(model, self.app.rotation.y, glm.vec3(0, 1, 0))  # Rotate around y-axis
        model = glm.rotate(model, self.app.rotation.z, glm.vec3(0, 0, 1))  # Rotate around z-axis
        if self.first_update:
            print("Model matrix after rotation in all dimensions:")
            print(self.app.mat_to_string(model))
            print(f"Rotation angle: {self.app.vec_to_string(glm.degrees(self.app.rotation))}")
            print()

        # Apply scaling
        model = glm.scale(model, glm.vec3(1.25, 1.25, 1.25))
        if self.first_update:
            print("Model matrix after scale of 1.25 in all dimensions:")
            print(self.app.mat_to_string(model))
            print()
            self.first_update = False  # Disable first update behavior after first run

        # Update the model matrix in the shader
        self.program['m_model'].write(model)