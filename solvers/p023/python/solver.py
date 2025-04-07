from math import sqrt, ceil
import time

def is_prime(n):
    k = ceil(sqrt(n))
    if n % 2 == 0:
        return False
    for i in range(3, k+1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_divisors(n):
    result = 0
    for i in range(1, n//2+1):
        result += i if n % i == 0 else 0
    return result

def main():
    # Get abundants
    abundants = []
    for i in range(1, 28123):
        if not is_prime(i):
            if sum_of_divisors(i) > i:
                abundants.append(i)
    
    inverse_list = [ a+b for a in abundants for b in abundants if a+b < 28123]
    target_list = set(range(1, 28123)) - set(inverse_list)
    total_sum = sum(target_list)

    print(f"{total_sum = }")

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")