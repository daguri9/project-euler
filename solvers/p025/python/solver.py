import time


def main():
    preb_fib = 1
    fib = 2
    digit_count = 1
    index = 3
    while digit_count < 1000:
        next_fib = fib + preb_fib
        preb_fib, fib = fib, next_fib
        digit_count = len(str(fib))
        index += 1

    print(f"{index = }")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
