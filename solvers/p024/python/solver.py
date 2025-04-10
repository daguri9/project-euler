import time
from math import factorial

def nth_perm(s, n):
    if factorial(len(s)) < n:
        raise ValueError("Not enough permutations.")
    if len(s) == 1:
        return s
    else:
        r = 1
        fact = factorial(len(s)-1)
        while fact * r < n:
            r += 1
        r -= 1
        return [s.pop(r)] + nth_perm(s, n-fact*r)

def main():
    input_numbers = list("0123456789")
    permutation  = nth_perm(input_numbers, 1_000_000)
    print(f"{''.join(permutation)}")
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
