import time
from math import ceil, sqrt


def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        k = ceil(sqrt(n))
        for i in range(3, k + 1, 2):
            if n % i == 0:
                return False
        return True


def check_perms(n, a, print_interval=100):
    c = [0 for i in range(n)]
    number = int("".join(a))
    curr_perm = 1
    largest = number if is_prime(number) else 0
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]
            number = int("".join(a))
            largest = number if number > largest and is_prime(number) else largest
            if curr_perm % print_interval == 0:
                print(f"Checking: {curr_perm}", end="\r")
            curr_perm += 1
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1
    return largest


def main():
    # The largest n-digit pandigital cannot have more than 9 digits
    input_list = list("123456789")
    found = False
    while not found:
        largest = check_perms(len(input_list), input_list.copy())
        found = False if largest == 0 else True
        input_list.pop()
    print()
    print(largest)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.7f} seconds.")
