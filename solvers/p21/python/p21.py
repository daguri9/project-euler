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
    for i in range(3, k+1, 2):
        if n % i == 0:
            return False
    return True

def primes_below(n):
    primes = []
    nxt_prime = n+1
    while nxt_prime > 2:
        nxt_prime = nearest_prime_below(nxt_prime)
        primes.append(nxt_prime)

    return primes

def sum_of_divisors(n):
    result = 0
    for i in range(1, n//2+1):
        result += i if n % i == 0 else 0
    return result

def main():
    primes = primes_below(10000)
    candidates = set(range(2, 10000)) - set(primes)
    amicables = []

    for i in candidates:
        if i not in amicables:
            b = sum_of_divisors(i)
            if b != i and i == sum_of_divisors(b):
                amicables.append(i)
                amicables.append(b)


    print(f"{amicables = }")
    total_sum = sum(amicables)
    print(f"{total_sum}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")