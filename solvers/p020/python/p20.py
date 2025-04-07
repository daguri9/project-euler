from math import factorial

def compute(n):
    digits = (str(factorial(n)))
    total_sum = 0
    for d in digits:
        total_sum += int(d)

    return total_sum


if __name__ == "__main__":
    print(compute(100))