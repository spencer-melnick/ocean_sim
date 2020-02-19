import random
import math
import matplotlib.pyplot as plt
import numpy as np

def generate_uniform_distribution(length):
    result = []

    for _ in xrange(length):
        result.append(random.uniform(0, 1))

    return result

def generate_gaussian_distribution(length):
    dist1 = generate_uniform_distribution(length)
    dist2 = generate_uniform_distribution(length)

    z1 = []
    z2 = []

    for x in xrange(length):
        U1 = dist1[x]
        U2 = dist2[x]

        A = math.sqrt(-2 * math.log(U1))
        theta = 2 * math.pi * U2

        Z1 = A * math.cos(theta)
        Z2 = A * math.sin(theta)

        z1.append(Z1)
        z2.append(Z2)

    return z1, z2

def main():
    u1 = generate_uniform_distribution(512)
    z1, _ = generate_gaussian_distribution(512)

    plt.subplot(121)
    plt.hist(z1, 5)
    plt.subplot(122)
    plt.hist(u1, 5)
    plt.show()

if __name__ == "__main__":
    main()
