#!/usr/bin/env python3

from vector2 import Vector2
import components
import ifft2

import sdl2.ext
import time
import math

def to_pixel_range(value):
    pixel_value = int(value * 255)

    if (pixel_value > 255):
        pixel_value = 255
    elif (pixel_value < 0):
        pixel_value = 0

    return pixel_value

def main():
    g = 9.81
    A = 1
    W = Vector2(28, 28)
    N = 32
    L = 100

    sdl2.ext.init()
    window = sdl2.ext.Window("Test", (N, N))
    window.show()

    renderer = sdl2.ext.Renderer(window)

    h0 = components.h0_tilde2(N, L, W, A, g)

    running = True

    start_time = time.time()

    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        current_time = time.time()
        t = (current_time - start_time) * 10

        h = components.h_tilde2(h0, t, N, L, W, A, g)
        y = ifft2.ifft2(h)

        for row in range(N):
            for column in range(N):
                num = to_pixel_range((y[row][column].real + 0.5) / 2)
                renderer.draw_point((column, row), sdl2.ext.Color(num, num, num))

        renderer.present()
        window.refresh()

if __name__ == "__main__":
    main()
