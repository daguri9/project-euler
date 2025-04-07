import time

def main():
    digits = list(str(2**1000))
    result = 0
    for d in digits:
        result += int(d)

    print(result)

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")