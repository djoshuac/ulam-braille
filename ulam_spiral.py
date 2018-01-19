#!/usr/bin/env python3

import argparse

from collections import namedtuple

def create_file(name, chunks):
    with open(name, "w") as fout:
        for chunk in chunks:
            fout.write(chunk)

def create_ppm(pixels):
    yield "P3\n"
    yield "{} {}\n".format(len(pixels), len(pixels[0]))
    yield "255\n"
    for row in pixels:
        for p in row:
            yield "\t{:3} {:3} {:3}".format(p.r, p.g, p.b)
        yield "\n"

def ulam_spiral(size):
    width = 2 * size + 1
    spiral = [[0]*width for _ in range(width)]
    n = 1
    pos = [size, size]
    dim = [1, 0]
    sign = [1, -1]
    try: # code would need to be more complex to handle the odd extra for loop for dims
        for s in range(width + 1):
            for d in dim:
                for _ in range(s):
                    spiral[pos[0]][pos[1]] = n
                    n += 1
                    pos[d] += sign[d]
                sign[d] *= -1
    except:
        return spiral

def prime_sieve(n):
    n += 1
    is_prime = [1] * n
    is_prime[0] = is_prime[1] = 0
    for i in range(n):
        if is_prime[i] == 1:
            for k in range(i**2, n, i):
                is_prime[k] += 1
    return is_prime

def create_is_prime(n):
    is_prime_cache = prime_sieve(n)

    def is_prime(n, is_prime_cache=is_prime_cache):
        if len(is_prime_cache) <= n:
            is_prime_cache = prime_sieve(n)
        return is_prime_cache[n]
    return is_prime

def transform(matrix, op):
    return [
        [op(m) for m in row]
        for row in matrix
    ]

def spiral_transpose(spiral, odd):
    transpose = []

if __name__ == "__main__":
    Pixel = namedtuple('Pixel', ['r', 'g', 'b'])
    parser = argparse.ArgumentParser(description='Ulam Spiral Generator')
    parser.add_argument('size', help='Number of spirals to generate')
    args = parser.parse_args()

    size = int(args.size)
    n = (size * 2 + 1)**2

    background = Pixel(0, 48, 103)
    prime_color = Pixel(200, 200, 200)

    colors = [
        background,
        prime_color,
        background,
        background,
        background,
        background,
        background,
        background,
        background,
        background,
        background,
        background
    ]

    # colors = [ # lotsa blue
    #     Pixel(255, 255, 255),
    #     Pixel(0, 0, 255),
    #     Pixel(100, 100, 255),
    #     Pixel(125, 125, 255),
    #     Pixel(150, 150, 255),
    #     Pixel(175, 175, 255),
    #     Pixel(220, 220, 255),
    #     Pixel(230, 230, 255),
    #     Pixel(255, 255, 255),
    #     Pixel(255, 255, 255),
    #     Pixel(255, 255, 255),
    #     Pixel(255, 255, 255),
    #     Pixel(255, 255, 255)
    # ]

    primality = create_is_prime(n)

    spiral = ulam_spiral(size)
    prime = transform(spiral, primality)
    pixels = transform(prime, lambda p: colors[p])

    create_file("primes.ppm", create_ppm(pixels))
