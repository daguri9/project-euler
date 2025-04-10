import time


def main():
    result = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
