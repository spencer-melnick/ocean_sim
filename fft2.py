import math

# Optionally import test libraries
if __name__ == "__main__":
    import copy
    import numpy as np

from complex import ComplexNumber

def reverse_bit(value, num_bits):
    result = 0

    for i in range(0, num_bits):
        new_bit_index = num_bits - (1 + i)
        bit_value = (value & (1 << i)) >> i

        result |= (bit_value << new_bit_index)

    return result

def generate_twidde(N):
    w = []

    for k in range(N // 2):
        power = ComplexNumber(0, 2 * math.pi * k / N)
        twiddle = ComplexNumber.exp(power)
        w.append(twiddle)

    for k in range(N // 2):
        w.append(-w[k])

    return w

def fft_horizontal(F, row_index = 0):
    N = len(F[row_index])
    num_steps = int(math.log(N, 2))

    # In place bit reverse the input
    for x in range(N // 2):
        y = reverse_bit(x, num_steps)

        temp = F[row_index][x]
        F[row_index][x] = F[row_index][y]
        F[row_index][y] = temp

    # Pregenerate twiddle factors
    w = generate_twidde(N)

    for step in range(num_steps):
        wing_length = pow(2, step)
        k_increment = wing_length * 2

        for n in range(N):
            if (n % k_increment) >= wing_length:
                # We are at the bottom of a wing, skip
                continue

            a_n = n
            b_n = a_n + wing_length

            # Perform a butterfly operation
            k = (a_n * N // k_increment) % N
            u = F[row_index][a_n]
            t = F[row_index][b_n] * w[k]

            F[row_index][a_n] = u + t
            F[row_index][b_n] = u - t

    return F

def fft_vertical(F, column_index = 0):
    N = len(F)
    num_steps = int(math.log(N, 2))

    # In place bit reverse the input
    for x in range(N // 2):
        y = reverse_bit(x, num_steps)

        temp = F[x][column_index]
        F[x][column_index] = F[y][column_index]
        F[y][column_index] = temp

    # Pregenerate twiddle factors
    w = generate_twidde(N)

    for step in range(num_steps):
        wing_length = pow(2, step)
        k_increment = wing_length * 2

        for n in range(N):
            if (n % k_increment) >= wing_length:
                # We are at the bottom of a wing, skip
                continue

            a_n = n
            b_n = a_n + wing_length

            # Perform a butterfly operation
            k = (a_n * N // k_increment) % N
            u = F[a_n][column_index]
            t = F[b_n][column_index] * w[k]

            F[a_n][column_index] = u + t
            F[b_n][column_index] = u - t

    return F

def fft2(f):
    F = copy.deepcopy(f)

    for row in range(len(F)):
        fft_horizontal(F, row)

    for column in range(len(F[0])):
        fft_vertical(F, column)

    return F


def main():
    seq = [
        [1, 0, -1, 0],
        [0, -1, 0, 1],
        [-1, 0, 1, 0],
        [0, 1, 0, -1]
        ]

    complex_seq = copy.deepcopy(seq)

    # Convert all real numbers to complex numbers
    for row in range(len(complex_seq)):
        for column in range(len(complex_seq[row])):
            complex_seq[row][column] = ComplexNumber(complex_seq[row][column])

    f = fft2(complex_seq)
    
    for row in f:
        row_string = ""
        for x in row:
            row_string += "{}, ".format(x)
        print(row_string)

    f = np.fft.fft2(seq)

    for x in f:
        print(x)

if __name__ == "__main__":
    main()
