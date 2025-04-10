import time


def get_sequence(n):
    current = n
    sequence = [n]
    while current > 1:
        current = current // 2 if current % 2 == 0 else 3 * current + 1
        sequence.append(current)

    return sequence


def main():
    candidate = 1
    largest = 1
    print_interval = 10000
    for i in range(1, 1_000_000):

        if i % print_interval == 0:
            print(f"Checking: {i}", end="\r")

        seq_length = len(get_sequence(i))
        if seq_length > largest:
            candidate = i
            largest = seq_length

    print()
    print(candidate)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
