import time


def main():
    total_sum = 0
    for i in range(1, 1001):
        total_sum += i**i
    print(str(total_sum)[-10:])


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
