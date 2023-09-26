using System;
using System.Collections.Generic;
using System.Drawing;

namespace PiroEngine
{
    public class DynamicTextureGenerator
    {
        private Dictionary<string, Bitmap> dynamicTextures;

        public DynamicTextureGenerator()
        {
            dynamicTextures = new Dictionary<string, Bitmap>();
        }

        public void CreateDynamicTexture(string textureName, int width, int height, Func<int, int, Color> textureFunction)
        {
            if (dynamicTextures.ContainsKey(textureName))
            {
                throw new ArgumentException($"Texture with name '{textureName}' already exists.");
            }

            Bitmap texture = new Bitmap(width, height);

            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    texture.SetPixel(x, y, textureFunction(x, y));
                }
            }

            dynamicTextures.Add(textureName, texture);
        }

        public Bitmap GetDynamicTexture(string textureName)
        {
            if (dynamicTextures.ContainsKey(textureName))
            {
                return dynamicTextures[textureName];
            }
            else
            {
                throw new ArgumentException($"Texture with name '{textureName}' does not exist.");
            }
        }
    }
}
