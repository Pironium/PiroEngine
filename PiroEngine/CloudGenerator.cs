using System;

public class CloudGenerator
{
    private Random random = new Random();

    public Cloud GenerateCloud()
    {
        int numParticles = random.Next(1000, 5000);
        var cloud = new Cloud();

        for (int i = 0; i < numParticles; i++)
        {
            float x = (float)random.NextDouble() * 100;
            float y = (float)random.NextDouble() * 50;
            float z = (float)random.NextDouble() * 100;
            float density = (float)random.NextDouble();

            cloud.AddParticle(new Particle(x, y, z, density));
        }

        return cloud;
    }
}
