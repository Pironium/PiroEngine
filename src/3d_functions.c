#include <stdio.h>
#include <math.h>

// Function to calculate the cross product of two 3D vectors
void crossProduct(float v1[3], float v2[3], float result[3]) {
    result[0] = v1[1] * v2[2] - v1[2] * v2[1];
    result[1] = v1[2] * v2[0] - v1[0] * v2[2];
    result[2] = v1[0] * v2[1] - v1[1] * v2[0];
}

// Function to normalize a 3D vector
void normalize(float vector[3]) {
    float magnitude = sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]);
    if (magnitude != 0) {
        vector[0] /= magnitude;
        vector[1] /= magnitude;
        vector[2] /= magnitude;
    }
}
