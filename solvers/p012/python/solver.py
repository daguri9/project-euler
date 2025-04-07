import time
from math import sqrt, ceil

def divisors(n):
    prime_factors = get_prime_factors(n)
    amount = 1
    for i in prime_factors.values():
        amount *= i + 1

    return amount

def is_prime(n):
    k = ceil(sqrt(n))
    if n % 2 == 0:
        return False
    for i in range(3, k+1, 2):
        if n % i == 0:
            return False
    return True

def nearest_prime_above(n):
    if n <= 1:
        return 2
    k = n + 2 if n % 2 != 0 else n + 1
    prime_found = is_prime(k)
    while not prime_found:
        k += 2
        prime_found = is_prime(k)
    
    return k

def get_prime_factors(n):
    cuotient = n
    prime = 2
    factors = {}
    while cuotient != 1:
        if cuotient % prime == 0:
            factors[prime] = 1 if prime not in factors else factors[prime] + 1
            cuotient /= prime
        else:
            prime = nearest_prime_above(prime)
    return factors


def main():
    n = 500
    triangle = 0
    divisor_count = 1
    i = 0
    while divisor_count < n:
        i += 1
        triangle += i
        divisor_count = divisors(triangle)

    print(triangle)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")