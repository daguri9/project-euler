import time
from math import ceil, sqrt


def is_prime(n):
    if n <= 0:
        return False
    k = ceil(sqrt(n))
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    candidates = [
        (a, b)
        for a in range(-999, 1000)
        for b in range(1, 1000)
        if b > abs(a) and is_prime(b) and is_prime(b + a + 1)
    ]

    best = None
    best_prime_count = 0
    for c in candidates:
        prime_count = 0
        a = c[0]
        b = c[1]
        i = 1
        while True:
            eq = i**2 + a * i + b
            if is_prime(eq):
                prime_count += 1
            else:
                break
            i += 1
        if prime_count > best_prime_count:
            best_prime_count = prime_count
            best = c

    print(f"{best = }")
    print(f"{best_prime_count = }")
    print(f"product = {best[0] * best[1]}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
