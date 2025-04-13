import time


def main():
    print_interval = 1000
    targets = []
    # Set upper bound as 9^5 * 6
    for i in range(10, (9**5) * 6):
        digits = list(str(i))
        digit_sum = sum(list(map(lambda x: int(x) ** 5, digits)))
        if i == digit_sum:
            targets.append(i)
        if i % print_interval == 0:
            print(f"Checking: {i}.", end="\r")
    print()
    print(f"{targets = }")
    print(f"sum: {sum(targets)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
