using System;
using System.Collections.Generic;

namespace PiroEngine
{
    public class Random3DObjectGenerator
    {
        private readonly Random _random = new Random();

        public List<GameObject> GenerateRandomObjects(int count)
        {
            var objects = new List<GameObject>();

            for (int i = 0; i < count; i++)
            {
                var position = new Vector3(
                    _random.Next(-100, 100),
                    _random.Next(-100, 100),
                    _random.Next(-100, 100)
                );

                var scale = new Vector3(
                    _random.Next(1, 10),
                    _random.Next(1, 10),
                    _random.Next(1, 10)
                );

                var rotation = new Vector3(
                    _random.Next(0, 360),
                    _random.Next(0, 360),
                    _random.Next(0, 360)
                );

                var object3D = new GameObject
                {
                    Name = "RandomObject" + i,
                    Position = position,
                    Scale = scale,
                    Rotation = rotation
                };

                objects.Add(object3D);
            }

            return objects;
        }
    }
}
