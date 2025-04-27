import time


def main():
    largest = 0
    for a in range(100):
        for b in range(100):
            dig_sum = sum([int(x) for x in str(a**b)])
            if dig_sum > largest:
                largest = dig_sum

    print(largest)

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
