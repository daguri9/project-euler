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


def main():
    for i in range(1488, 10000):
        fst = i
        snd = i + 3330
        trd = i + 3330 * 2

        if set(str(fst)) == set(str(snd)) and set(str(fst)) == set(str(trd)):
            if is_prime(fst) and is_prime(snd) and is_prime(trd):

                print(f"{fst}{snd}{trd}")
                break


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
