import time


def main():
    terms = {a**b for a in range(2, 101) for b in range(2, 101)}
    print(f"Distinct terms: {len(terms)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
