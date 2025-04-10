import time


def main():
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            candidate = str(i * j)
            if candidate == candidate[::-1]:
                print(f"{candidate} with numbers {i} and {j}.")
                return


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
