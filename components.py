#!/usr/bin/env python3

import math
import gaussian
from vector2 import Vector2
from complex import ComplexNumber

if __name__ == "__main__":
    from PIL import Image

def to_k(n, m, N, M, L):
    kx = math.pi * (2 * n - N) / L
    ky = math.pi * (2 * m - N) / L
    return Vector2(kx, ky)

def from_k(k, N, M, L):
    n = ((L * k.x / math.pi) + N) / 2
    m = ((L * k.y / math.pi) + N) / 2
    return (n, m)

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
            k = to_k(row, column, N, N, L)

            if (k.x == 0) and (k.y == 0):
                F[row].append(ComplexNumber(0))
                continue

            F[row].append(h0_tilde(k, W, g1[row][column], g2[row][column], A, g))

    return F

def h_tilde2(h0, t, N, L, W, A = 1, g = 9.81):
    h = []

    for row in range(N):
        h.append([])
        for column in range(N):
            n1 = row
            m1 = column

            n2 = N - row
            m2 = N - column

            if (n2 == N):
                n2 = n1
            if (m2 == N):
                m2 = m1

            k = to_k(n1, m1, N, N, L)

            if (k.x == 0 and k.y == 0):
                h[row].append(ComplexNumber(0))
                continue

            w = math.sqrt(k.magnitude() / g)

            component = h0[n1][m1] * ComplexNumber.exp(ComplexNumber(0, w * t)) + h0[n2][m2].conjugate() * ComplexNumber.exp(ComplexNumber(0, -w * t))
            h[row].append(component)

    return h


def main():
    g = 9.81
    A = 4
    W = Vector2(28, 28)
    N = 256
    L = 1000

    h0_t = h0_tilde2(N, L, W, A, g)
    h_t = h_tilde2(h0_t, 0, N, L, W, A, g)

    h_image = Image.new(mode = "RGB", size = (N, N))
    h_pixels = h_image.load()

    for row in range(N):
        for column in range(N):
            num = h_t[row][column]
            h_pixels[row, column] = (int(255 * num.real), int(255 * num.imaginary), 0)

    h_image.show()
    h_image.save("test.png", "PNG")
        


if __name__ == "__main__":
    main()
