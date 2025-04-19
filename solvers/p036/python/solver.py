import time


def main():
    total_sum = 0
    for i in range(1_000_000):
        i_str = str(i)
        bin_str = bin(i)[2:]
        if i_str[::-1] == i_str and bin_str[::-1] == bin_str:
            total_sum += i
    
    print(f"{total_sum}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
