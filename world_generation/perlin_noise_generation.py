import numpy as np

class PerlinNoiseGenerator:
    def __init__(self, seed=None):
        self.seed = seed
        self.permutation_table = np.random.permutation(512)
        self.p = np.arange(512, dtype=int)
        if seed is not None:
            np.random.seed(seed)
            np.random.shuffle(self.p)
            self.p = np.concatenate((self.p, self.p))

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash, x):
        h = hash & 15
        grad = 1 + (h & 7)
        if h & 8:
            grad = -grad
        return (grad * x)

    def generate_perlin_noise(self, width, height, scale):
        noise_map = np.zeros((height, width))
        if self.seed is not None:
            np.random.seed(self.seed)

        for y in range(height):
            for x in range(width):
                x_scaled = x / scale
                y_scaled = y / scale

                X = int(x_scaled) & 255
                Y = int(y_scaled) & 255

                x_frac = x_scaled - int(x_scaled)
                y_frac = y_scaled - int(y_scaled)

                u = self.fade(x_frac)
                v = self.fade(y_frac)

                A = self.p[X] + Y
                B = self.p[X + 1] + Y

                aa, ab, ba, bb = self.p[A], self.p[A + 1], self.p[B], self.p[B + 1]

                grad_aa = self.grad(aa, x_frac)
                grad_ab = self.grad(ab, x_frac - 1)
                grad_ba = self.grad(ba, x_frac)
                grad_bb = self.grad(bb, x_frac - 1)

                lerp_x1 = self.lerp(u, grad_aa, grad_ab)
                lerp_x2 = self.lerp(u, grad_ba, grad_bb)

                noise_map[y][x] = self.lerp(v, lerp_x1, lerp_x2)

        return noise_map
