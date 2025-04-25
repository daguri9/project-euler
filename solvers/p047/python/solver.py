import time
from math import sqrt

cache_1 = {}


def is_prime(n):
    if n in cache_1:
        return cache_1[n]
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        k = int(sqrt(n))
        for i in range(3, k + 1, 2):
            if n % i == 0:
                cache_1[n] = False
                return False
        cache_1[n] = True
        return True


cache_2 = {}


def nearest_prime_above(n):
    if n in cache_2:
        return cache_2[n]
    if n <= 1:
        return 2
    k = n + 2 if n % 2 != 0 else n + 1
    prime_found = is_prime(k)
    while not prime_found:
        k += 2
        prime_found = is_prime(k)

    cache_2[n] = k
    return k


cache_3 = {}


def count_prime_factors(n):
    if n in cache_3:
        return cache_3[n]
    cuotient = n
    prime = 2
    factors = set()
    while cuotient != 1:
        if cuotient % prime == 0:
            factors.add(prime)
            cuotient /= prime
        else:
            prime = nearest_prime_above(prime)
    cache_3[n] = len(factors)
    return len(factors)


def main():
    print_int = 1000
    i = 1
    found = False
    while not found:
        if i % print_int == 0:
            print(f"Checking: {i}", end="\r")

        factor_counts = [count_prime_factors(i + x) for x in range(4)]

        if all(x == 4 for x in factor_counts):
            print()
            print(f"{i}, {i+1}, {i+2}, {i+3}")
            found = True
        i += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
