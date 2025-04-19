import time
from math import ceil, sqrt


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


def primes_below(n):
    primes = []
    nxt_prime = n + 1
    while nxt_prime > 2:
        nxt_prime = nearest_prime_below(nxt_prime)
        primes.append(nxt_prime)

    return primes


def is_circular(p):
    p_str = str(p)
    for i in range(1, len(p_str)):
        rot = int(p_str[-i:] + p_str[: len(p_str) - i])
        if not is_prime(rot):
            return False
    return True


def main():
    primes = primes_below(1_000_000)
    circ_primes = []
    count = 0
    for i in primes:
        count += 1 if is_circular(i) else 0
    print(f"{count}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
