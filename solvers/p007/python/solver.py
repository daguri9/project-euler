import time


def nth_prime(n, print_interval=100):
    ith = 1
    prime_cand = 1
    iterations = 0
    while ith < n:
        prime_cand += 2
        iterations += 1
        if iterations % print_interval == 0:
            print(f"Checking: {ith= }", end="\r")
        if is_prime(prime_cand):
            ith += 1
    print()
    return prime_cand


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    print(nth_prime(10001))


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
