using System;
using UnityEngine;

public class PiroTextureGenerator
{
    public static Texture2D GenerateDynamicTexture(int width, int height)
    {
        Texture2D texture = new Texture2D(width, height);

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                Color pixelColor = GenerateNoiseTextureColor(x, y);
                texture.SetPixel(x, y, pixelColor);
            }
        }

        texture.Apply();
        return texture;
    }

    private static Color GenerateNoiseTextureColor(int x, int y)
    {
        // Здесь мы могли бы использовать сложные математические функции для создания уникальных шумовых текстур.
        float red = Mathf.PerlinNoise(x * 0.1f, y * 0.1f);
        float green = Mathf.PerlinNoise(x * 0.2f, y * 0.2f);
        float blue = Mathf.PerlinNoise(x * 0.3f, y * 0.3f);

        return new Color(red, green, blue);
    }
}
