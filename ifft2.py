import math
import fft2

def ifft2(f):
    F = fft2.fft2(f)

    N = len(F)
    M = len(F[0])

    for row in range(N):
        for column in range(M):
            F[row][column] *= math.pow(-1, row) * math.pow(-1, column) / (N * M)

    return F

