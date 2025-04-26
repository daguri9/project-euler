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


def nearest_prime_below(n):
    if n == 3:
        return 2
    k = n - 2 if not n % 2 == 0 else n - 1
    for i in range(k, 1, -2):
        if is_prime(i):
            return i

    return -1


def primes_below(n):
    primes = []
    nxt_prime = n + 1
    while nxt_prime > 2:
        nxt_prime = nearest_prime_below(nxt_prime)
        primes.append(nxt_prime)

    return primes


def main():
    print_interval = 2000
    target = 1000_000
    primes = primes_below(target // 8)
    primes.reverse()
    largest = 0
    best_sequence = []
    print(f"{len(primes) = }")
    for i in range(10):
        for j in range(i + 1 + len(best_sequence), len(primes)):
            sequence = primes[i:j]
            seq_sum = sum(sequence)
            if seq_sum < target and is_prime(seq_sum):
                largest = seq_sum
                best_sequence = sequence
            if j % print_interval == 0:
                print(
                    f"Checking: {i}, len: {j-i}, overshooting: {seq_sum >= target}, largest sequence: {len(best_sequence)}",
                    end="\r",
                )

    print()
    print(best_sequence)
    print(largest)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
