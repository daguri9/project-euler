import time
import matplotlib.pyplot as plt
from math import sqrt


cache = {}


def pent(n):
    if n in cache:
        return cache[n]
    cache[n] = int(n * (3 * n - 1) / 2)
    return cache[n]


def is_pent(k):
    n = (1 + sqrt(1 + 24 * k)) / 6
    return n.is_integer()


def main():
    print_interval = 100

    for k in range(1, 3000):
        for j in range(k + 1, 3000):
            j_pent = pent(j)
            k_pent = pent(k)
            if j % print_interval == 0:
                print(f"Checking: {j = }", end="\r")
            if is_pent(j_pent - k_pent) and is_pent(k_pent + j_pent):
                print()
                print(f"{j_pent = }, {k_pent = }, D = {j_pent - k_pent}")
                return


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
