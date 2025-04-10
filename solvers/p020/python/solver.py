from math import factorial
import time


def main():
    n = 100
    digits = str(factorial(n))
    total_sum = 0
    for d in digits:
        total_sum += int(d)

    print(total_sum)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
