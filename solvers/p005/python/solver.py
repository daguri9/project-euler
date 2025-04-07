import time

def main():
    n = 20
    candidate = n
    while True:
        discard = False
        for i in range(1, n+1):
            if candidate % i != 0:
                discard = True
                break
        if discard:
            candidate += 1
        else:
            print(candidate)
            return


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")