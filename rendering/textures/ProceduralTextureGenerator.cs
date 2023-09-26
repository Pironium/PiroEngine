using System;

namespace PiroEngine
{
    public class ProceduralTextureGenerator
    {
        public Texture GeneratePerlinNoiseTexture(int width, int height, float scale)
        {
            Texture texture = new Texture(width, height);

            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    float xCoord = (float)x / width * scale;
                    float yCoord = (float)y / height * scale;
                    
                    float noiseValue = PerlinNoise(xCoord, yCoord);
                    
                    Color color = new Color(noiseValue, noiseValue, noiseValue);
                    texture.SetPixel(x, y, color);
                }
            }

            return texture;
        }

        private float PerlinNoise(float x, float y)
        {
            // Реализация алгоритма Perlin Noise здесь
            // ...
        }
    }
}
