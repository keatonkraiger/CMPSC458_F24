# ModernGL Triangle Renderer: Class Overviews

## Creating a Triangle Renderer

To run our program, we will run the `tutorial_1.py` file. In this file, we create an instance of the `Engine` class and call its `run` method.

## Engine Class

The Engine class serves as the main controller for our application. Its primary responsibilities include:

1. Initializing Pygame and creating an OpenGL context
2. Setting up the rendering pipeline (shaders, VBO, VAO)
3. Managing the main game loop
4. Handling events (like quitting the application)
5. Coordinating the rendering process

Think of the Engine class as the main "game loop" that keeps everything running smoothly.

## VBO (Vertex Buffer Object) Class

The VBO class handles the vertex data for our triangle. Its main tasks include:

1. Defining the vertex data (positions and colors)
2. Creating a buffer on the GPU to store this data

You can think of the VBO as the "raw ingredients" of our triangle - it holds all the data that defines what our triangle looks like.

## Shader Class

The Shader class is responsible for managing our OpenGL shaders. Its key functions are:

1. Loading vertex and fragment shaders from files
2. Compiling and linking shaders into a shader program
3. Providing access to the shader program for use in rendering

Shaders are like the instructions for how our GPU should draw things. The Shader class ensures these instructions are properly loaded and ready to use.

## Vertex Shader (default.vert)

The vertex shader is the first stage in the rendering pipeline. It processes each vertex of our triangle individually. Here's what each part does:

1. `#version 330 core`: Specifies the version of GLSL to use
2. `layout (location = 0) in vec3 in_position`: This declares an input variable for the vertex position. It's a 3D vector (x, y, z)
3. `layout (location = 1) in vec3 in_color`: This declares an input variable for the vertex color. It's a 3D vector (r, g, b)
4. `out vec3 v_color`: This declares an output variable for the fragment shader. It's a 3D vector (r, g, b)
5. `gl_Position = vec4(in_position, 1.0)`: This sets the position of the vertex. We convert the 3D position to a 4D vector (x, y, z, w) where w is 1.0
6. `v_color = in_color`: This passes the color data to the fragment shader

## Fragment Shader (default.frag)

The fragment shader runs for each pixel (fragment) that will be drawn to the screen. It determines the final color of each pixel. Here's what each part does:

1. `#version 330 core`: Specifies the version of GLSL to use
2. `in vec3 v_color`: This declares an input variable for the color passed from the vertex shader
3. `out vec4 f_color`: This declares the output color. It's a 4D vector (r, g, b, a) where 'a' is the alpha (transparency) value.
4. `f_color = vec4(v_color, 1.0)`: This sets the final color of the fragment to the color passed from the vertex shader.

## Vertex and Fragment Shaders

The vertex and fragment shaders work together to define how our triangle is drawn. Specifically:

1. The vertex shader processes each vertex of our triangle, setting its position and passing along its color
2. OpenGL uses these processed vertices to determine which pixels on the screen are inside the triangle.
3. For each of these pixels, the fragment shader runs, interpolating the color values from the vertices and setting the final color of the pixel.
 

## VAO (Vertex Array Object) Class

The VAO class acts as a bridge between our vertex data (VBO) and our shader program. Its primary function is:

1. Setting up the attribute pointers that tell the GPU how to interpret our vertex data

The VAO is like a recipe that tells the GPU how to use our "ingredients" (VBO) with our "cooking instructions" (Shader) to create our final "dish" (rendered triangle).

## Program Flow

1. The Engine initializes everything and starts the main loop.
2. In each frame of the main loop:
    - The Engine checks for events (like quitting).
    - It then calls the render method, which:
        - Clears the screen
        - Tells the VAO to render (which uses the VBO data and Shader program)
        - Flips the display to show the new frame

This process repeats continuously, creating the illusion of a persistent triangle on the screen.