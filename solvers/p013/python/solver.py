import time

def main():
    with open('numbers.txt') as f:
        numbers = [int(line) for line in f]

    print(str(sum(numbers))[:10])

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")