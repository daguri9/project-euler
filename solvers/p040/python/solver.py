import time
from math import prod


def main():
    target_elems = []
    n = 0  # nth
    n_dig = 1  # Number of digits of each i
    d = 1  # Next number before increase of digits of i
    i = 1
    targets = [10**i for i in reversed(range(7))]
    while len(targets) > 0:
        n += n_dig
        if n >= targets[-1]:
            target_elems.append(int(str(i)[targets.pop() - n - 1]))
        i += 1
        if i == d * 10:
            n_dig += 1
            d *= 10
    print(prod(target_elems))


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
