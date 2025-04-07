def compute(n):
    squares_sum = sum([i**2 for i in range(n+1)])
    sum_squares = sum([i for i in range(n+1)])**2
    print(f"{squares_sum = }")
    print(f"{sum_squares = }")
    diff = abs(squares_sum - sum_squares)
    return diff


if __name__ == "__main__":
    print(compute(100))