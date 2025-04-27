import time
from math import comb

def main():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if comb(n, r) > 1_000_000:
                count += 1
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
