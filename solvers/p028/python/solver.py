import time


def main():
    size = 3
    diag_sum = 1
    i = 1
    corners = 0
    while size <= 1001:
        step = size - 1
        i += step
        diag_sum += i
        corners += 1
        if corners == 4:
            corners = 0
            size += 2

    print(f"{diag_sum = }")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
