from math import comb
import time

def main():
    n = 20
    print(comb(n+n, n))

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")