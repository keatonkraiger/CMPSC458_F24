import pygame as pg

class Texture:
    def __init__(self, context):
        self.context = context
        self.textures = {}
        self.textures['container'] = self.get_texture('Media2/textures/container.jpg')
        self.textures['awesomeface'] = self.get_texture('Media2/textures/awesomeface.png', alpha=True, flip=False)
         
    def get_texture(self, path, alpha=False, flip=True):
        """ Load a texture from a given path and return it as a moderngl texture object.

        Args:
            path (str): The path to the texture file. 
            alpha (bool, optional): A flag to indicate if the texture has an alpha channel. Defaults to False.
            flip (bool, optional): Flag to indicate if the texture should be flipped. Defaults to True.

        Returns:
            moderngl.Texture: A moderngl texture object.
        """
        texture = pg.image.load(path)
        texture = pg.transform.flip(texture, False, flip)
        if alpha:
            texture = texture.convert_alpha()
            components = 4
            format = 'RGBA'
        else:
            texture = texture.convert()
            components = 3
            format = 'RGB'
        
        texture_data = pg.image.tostring(texture, format)
        texture = self.context.texture(
            size=texture.get_size(),
            components=components,
            data=texture_data
        )
        return texture

    def destroy(self):
        for texture in self.textures.values():
            texture.release()