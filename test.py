#!/usr/bin/env python3

import gaussian
from PIL import Image

def main():
    uniform_image = Image.new(mode = "L", size = (512, 512))
    uniform_pixels = uniform_image.load()

    gaussian_image = Image.new(mode = "L", size = (512, 512))
    gaussian_pixels = gaussian_image.load()

    for row in range(512):
        uniform_noise = gaussian.generate_uniform_distribution(512)
        gaussian_noise, _ = gaussian.generate_gaussian_distribution(512)

        for column in range(512):
            uniform_pixels[row, column] = int(uniform_noise[column] * 255)
            gaussian_pixels[row, column] = int((gaussian_noise[column] + 2.5) * 255 / 5)

    uniform_image.show()
    gaussian_image.show()

if __name__ == "__main__":
    main()
