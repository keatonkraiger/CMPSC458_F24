import glm
import pygame as pg

FOV = 100  # Field of View in degrees
NEAR = 0.1  # Near clipping plane
FAR = 100  # Far clipping plane
SPEED = 5  # Camera movement speed
SENSITIVITY = 0.05  # Mouse sensitivity

class Camera:
    """
    A camera class for 3D scene navigation.

    This class handles camera movement, rotation, and perspective calculations
    for a 3D environment.
    """

    def __init__(self, app, position=(0,0,-3), yaw=90, pitch=0):
        """
        Initialize the camera with given parameters.

        Args:
            app: The main application object.
            position (tuple): Initial position of the camera (x, y, z).
            yaw (float): Initial yaw angle in degrees.
            pitch (float): Initial pitch angle in degrees.
        """
        self.app = app
        self.aspect_ratio = app.window_size[0] / app.window_size[1]
        self.position = glm.vec3(position)
        self.yaw = yaw
        self.pitch = pitch
        
        # Initialize camera vectors
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, 1)
        
        # Calculate initial view and projection matrices
        self.m_view = self.get_view_matrix()
        self.m_projection = self.get_projection_matrix()
     
    def rotate(self):
        """
        Rotate the camera based on mouse movement.
        """
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))  # Clamp pitch to avoid gimbal lock
        
    def update_camera_vectors(self):
        """
        Update the camera's directional vectors based on yaw and pitch.
        """
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch) 
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)
        
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
        
    def update(self):
        """
        Update the camera's orientation and view matrix.
        """
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()
    
            
    def get_projection_matrix(self):
        """
        Calculate and return the projection matrix.

        Returns:
            glm.mat4: The projection matrix.
        """
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def get_view_matrix(self):
        """
        Calculate and return the view matrix.

        Returns:
            glm.mat4: The view matrix.
        """
        return glm.lookAt(self.position, self.position + self.forward, self.up)