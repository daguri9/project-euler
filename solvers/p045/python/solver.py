import time
from math import sqrt


def is_tri(t):
    n = (1 / 2) * (sqrt(8 * t + 1) - 1)
    return n.is_integer()


def is_pent(p):
    n = (1 + sqrt(1 + 24 * p)) / 6
    return n.is_integer()


def is_hex(h):
    n = (1 + sqrt(8 * h + 1)) / 4
    return n.is_integer()


def get_hex(n):
    return n * (2 * n - 1)


def main():
    i = 144
    while True:
        n = get_hex(i)
        if is_tri(n) and is_pent(n):
            print(n)
            break
        i += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
