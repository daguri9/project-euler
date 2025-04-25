import time
from math import sqrt, ceil


def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        k = ceil(sqrt(n))
        for i in range(3, k + 1, 2):
            if n % i == 0:
                return False
        return True


def find_decomposition(n):
    sqr = int(sqrt(n))
    for i in reversed(range(1, sqr)):
        double_sqr = 2 * i**2
        if double_sqr < n and is_prime(n - double_sqr):
            return (n - double_sqr, i)
    return None


def main():
    found = False
    n = 9
    while not found:
        if n % 2 != 0 and not is_prime(n):
            decomp = find_decomposition(n)
            if decomp == None:
                print(n)
                found = True
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
