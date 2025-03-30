import time

def compute():
    candidate = 1
    largest = 1
    for i in range(1, 1_000_000):

        if i % 1000:
            print(f"{i = }", end="\r")

        seq_length = len(get_sequence(i))
        if seq_length > largest:
            candidate = i
            largest = seq_length

    print()
    return candidate

def get_sequence(n):
    current = n
    sequence = [n]
    while current > 1:
        current = current // 2 if current % 2 == 0 else 3*current + 1
        sequence.append(current)

    return sequence

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")