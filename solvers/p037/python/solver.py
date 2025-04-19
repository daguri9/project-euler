import time
from math import ceil, sqrt


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


def next_prime(n):
    i = n + 1
    while not is_prime(i):
        i += 1
    return i


def main():
    truncatables = []
    i = 13
    while len(truncatables) < 11:
        is_trunc = True
        for k in range(1, len(str(i))):
            sub_l = int(str(i)[k:])
            sub_r = int(str(i)[: len(str(i)) - k])
            if not is_prime(sub_l) or not is_prime(sub_r):
                is_trunc = False
                break
        if is_trunc:
            truncatables.append(i)
        i = next_prime(i)

    print(f"{truncatables}")
    print(f"{sum(truncatables)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
