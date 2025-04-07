import time

def main():
    triplets = [(a, b, c) for a in range(1, 1000) for b in range(1, 1000) for c in range(1, 1000) if c > b and b > a and a + b + c == 1000 and a**2 + b**2 == c**2][0]
    print(f"{triplets = }")
    print(triplets[0] * triplets[1] * triplets[2])

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
