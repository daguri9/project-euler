import time


def main():
    i = 2
    print_interval = 1000
    while True:
        if i % print_interval == 0:
            print(f"Checking: {i}", end='\r')
        digits = set(str(i))
        if all(set(str(i*x)) == digits for x in range(2, 7)):
            print()
            print(i)
            print([i*x for x in range(2, 7)])
            break
        i += 1

            


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
