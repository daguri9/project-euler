from math import sqrt
from math import ceil
import time


def largest_prime_factor(n, print_interval=1000):
    k = nearest_prime_below(ceil(sqrt(n)))
    iterations = 0
    while k > 2:
        iterations += 1
        if iterations % print_interval == 0:
            print(f"Checking: {k}", end="\r")

        if n % k == 0:
            print()
            return k
        else:
            k = nearest_prime_below(k)


def nearest_prime_below(n):
    k = n - 2 if not n % 2 == 0 else n - 1
    for i in range(k, 1, -2):
        if is_prime(i):
            return i

    return -1


def is_prime(n):
    k = ceil(sqrt(n))
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, k+1, 2):
        if n % i == 0:
            return False
    return True

def main():
    print(largest_prime_factor(600851475143))


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
