// RayTracing.java - PiroEngine Ray Tracing Renderer

import java.util.ArrayList;
import java.util.List;

public class RayTracing {

    // Define a class for representing a 3D vector
    private static class Vec3 {
        double x, y, z;

        public Vec3(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public Vec3 add(Vec3 other) {
            return new Vec3(this.x + other.x, this.y + other.y, this.z + other.z);
        }

        public Vec3 subtract(Vec3 other) {
            return new Vec3(this.x - other.x, this.y - other.y, this.z - other.z);
        }

        public Vec3 multiply(double scalar) {
            return new Vec3(this.x * scalar, this.y * scalar, this.z * scalar);
        }

        public double dot(Vec3 other) {
            return this.x * other.x + this.y * other.y + this.z * other.z;
        }

        public Vec3 cross(Vec3 other) {
            return new Vec3(
                this.y * other.z - this.z * other.y,
                this.z * other.x - this.x * other.z,
                this.x * other.y - this.y * other.x
            );
        }

        public double length() {
            return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
        }

        public Vec3 normalize() {
            double len = this.length();
            return new Vec3(this.x / len, this.y / len, this.z / len);
        }
    }

    // Define a class for representing a ray
    private static class Ray {
        Vec3 origin;
        Vec3 direction;

        public Ray(Vec3 origin, Vec3 direction) {
            this.origin = origin;
            this.direction = direction;
        }

        public Vec3 pointAt(double t) {
            return origin.add(direction.multiply(t));
        }
    }

    // Define a class for representing a 3D sphere
    private static class Sphere {
        Vec3 center;
        double radius;

        public Sphere(Vec3 center, double radius) {
            this.center = center;
            this.radius = radius;
        }

        public boolean hit(Ray ray, double tMin, double tMax) {
            Vec3 oc = ray.origin.subtract(this.center);
            double a = ray.direction.dot(ray.direction);
            double b = oc.dot(ray.direction);
            double c = oc.dot(oc) - this.radius * this.radius;
            double discriminant = b * b - a * c;

            if (discriminant > 0) {
                double temp = (-b - Math.sqrt(discriminant)) / a;
                if (temp < tMax && temp > tMin) {
                    return true;
                }
                temp = (-b + Math.sqrt(discriminant)) / a;
                if (temp < tMax && temp > tMin) {
                    return true;
                }
            }
            return false;
        }
    }

    // Define a class for the scene
    private static class Scene {
        List<Sphere> spheres = new ArrayList<>();

        public void addSphere(Sphere sphere) {
            spheres.add(sphere);
        }

        public boolean hit(Ray ray, double tMin, double tMax) {
            boolean hitAnything = false;
            double closestSoFar = tMax;

            for (Sphere sphere : spheres) {
                if (sphere.hit(ray, tMin, closestSoFar)) {
                    hitAnything = true;
                    closestSoFar = ray.pointAt(tMax).subtract(ray.origin).length();
                }
            }

            return hitAnything;
        }
    }

    // Main rendering function
    public static void render(Scene scene) {
        int imageWidth = 800;
        int imageHeight = 600;

        // Create an image buffer for storing the rendered image
        int[][] image = new int[imageWidth][imageHeight];

        // Define the camera parameters
        Vec3 cameraPosition = new Vec3(0, 0, -1);
        Vec3 cameraLowerLeftCorner = new Vec3(-2, -1, -1);
        Vec3 cameraHorizontal = new Vec3(4, 0, 0);
        Vec3 cameraVertical = new Vec3(0, 2, 0);

        // Render the scene
        for (int j = imageHeight - 1; j >= 0; j--) {
            for (int i = 0; i < imageWidth; i++) {
                double u = (double) i / (imageWidth - 1);
                double v = (double) j / (imageHeight - 1);

                Ray ray = new Ray(
                    cameraPosition,
                    cameraLowerLeftCorner.add(cameraHorizontal.multiply(u)).add(cameraVertical.multiply(v))
                );

                if (scene.hit(ray, 0.0, Double.POSITIVE_INFINITY)) {
                    image[i][j] = 0xFF0000; // Red color for hit
                } else {
                    image[i][j] = 0xFFFFFF; // White color for miss
                }
            }
        }

        // Save the rendered image to a file or display it
        // (Code to save or display the image goes here...)
    }

    public static void main(String[] args) {
        // Create a scene with spheres
        Scene scene = new Scene();
        scene.addSphere(new Sphere(new Vec3(0, 0, -1), 0.5));
        scene.addSphere(new Sphere(new Vec3(0, -100.5, -1), 100));

        // Render the scene using ray tracing
        render(scene);
    }
}
