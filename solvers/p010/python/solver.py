from math import sqrt, ceil
import time


def nearest_prime_below(n):
    if n == 3:
        return 2
    k = n - 2 if not n % 2 == 0 else n - 1
    for i in range(k, 1, -2):
        if is_prime(i):
            return i

    return -1


def is_prime(n):
    k = ceil(sqrt(n))
    if n % 2 == 0:
        return False
    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    n = 2_000_000
    next_prime = nearest_prime_below(n)
    total_sum = 0
    while next_prime != -1:
        total_sum += next_prime
        next_prime = nearest_prime_below(next_prime)

    print(total_sum)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
