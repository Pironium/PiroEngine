#version 330 core

uniform vec3 cameraPosition;
uniform float time;

in vec3 fragPosition;

out vec4 fragColor;

void main() {
    // Calculate the water color based on time and camera position
    vec3 waterColor = vec3(0.0, 0.5, 1.0) + vec3(0.1, 0.1, 0.1) * sin(time);

    // Calculate the distortion of the water surface
    float distortion = sin(fragPosition.x * 10.0 + time) + sin(fragPosition.z * 10.0 + time);

    // Calculate the final fragment color with distortion
    fragColor = vec4(waterColor * distortion, 1.0);
}
