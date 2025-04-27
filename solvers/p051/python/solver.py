import time
from math import sqrt
from itertools import combinations

cache = {}


def is_prime(n):
    if n in cache:
        return cache[n]
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        k = int(sqrt(n))
        for i in range(3, k + 1, 2):
            if n % i == 0:
                cache[n] = False
                return False
        cache[n] = True
        return True


def main():
    print_interval = 1000
    n = 1
    family = []
    found = False
    while not found:
        if n % print_interval == 0:
            print(f"Checking: {n}", end="\r")
        n += 1
        if not is_prime(n):
            continue
        n_str = str(n)
        for k in range(1, len(n_str)):
            # Try every selection of k digits
            for i in combinations(range(len(n_str) - 1), k):
                f = []
                for j in range(10):
                    member = n_str
                    for index in i:
                        member = member[:index] + str(j) + member[index + 1 :]
                    if member[0] == "0":
                        continue
                    if is_prime(int(member)):
                        f.append(int(member))
                if len(f) > len(family):
                    family = f
                    if len(family) == 9:
                        found = True
                        break
            if found:
                break
    print()
    print(family)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
