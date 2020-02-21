#!/usr/bin/env python3

import math
import gaussian
from vector2 import Vector2
from complex import ComplexNumber

if __name__ == "__main__":
    from PIL import Image

def phillips(K, W, A = 1, g = 9.81):
    L = W.magnitude2() / g
    l = L / 1000
    k = K.normalized()
    w = W.normalized()

    k2 = K.magnitude2()

    dot = Vector2.dot(k, w)
    dot2 = dot * dot

    return A * math.exp(-1 / (k2 * L * L)) * dot2 * math.exp(-k2 * l * l) / (k2 * k2)

def h0_tilde(K, W, r, i, A = 1, g = 9.81):
    return (1 / math.sqrt(2)) * ComplexNumber(r, i) * math.sqrt(phillips(K, W, A, g))

def h0_tilde2(N, L, W, A = 1, g = 9.81):
    '''
    :param int N: Number of points to be sampled
    :param int L: Length of patch in meters
    :param Vector2 W: Wind speed
    :param float A: Wave amplitude
    :param float g: Gravitational constant
    '''
    F = []

    g1, g2 = gaussian.gaussian2(N, N)

    for row in range(N):
        F.append([])
        for column in range(N):
            kx = math.pi * (2 * column - N) / L
            ky = math.pi * (2 * row - N) / L
            k = Vector2(kx, ky)

            if (kx == 0) and (ky == 0):
                F[row].append(ComplexNumber(0))
                continue

            F[row].append(h0_tilde(k, W, g1[row][column], g2[row][column], A, g))

    return F


def main():
    g = 9.81
    A = 4
    W = Vector2(30, 30)
    N = 256
    L = 1000

    h0_t = h0_tilde2(N, L, W, A, g)

    h0_image = Image.new(mode = "RGB", size = (N, N))
    h0_pixels = h0_image.load()

    for row in range(N):
        for column in range(N):
            num = h0_t[row][column]
            h0_pixels[row, column] = (int(255 * num.real), int(255 * num.imaginary), 0)

    h0_image.show()
        


if __name__ == "__main__":
    main()
