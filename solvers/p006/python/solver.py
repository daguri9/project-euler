import time

def main():
    n = 100
    squares_sum = sum([i**2 for i in range(n+1)])
    sum_squares = sum([i for i in range(n+1)])**2
    print(f"{squares_sum = }")
    print(f"{sum_squares = }")
    diff = abs(squares_sum - sum_squares)
    print(diff)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")