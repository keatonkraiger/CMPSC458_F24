#version 330 core

layout (location = 0) in vec2 in_texcoord_0;
layout (location = 1) in vec3 in_position;

out vec2 TexCoord;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

void main() {
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
    TexCoord = vec2(in_texcoord_0.x, 1.0 - in_texcoord_0.y);
}
