import time
from math import sqrt


def get_solutions(p):
    a, b, c = 0


def main():
    largest = 0
    solutions = []

    for p in range(1, 1001):
        ul = p // 2 + 1
        p_sols = [
            (a, b, int(c))
            for a in range(1, ul)
            for b in range(1, ul)
            if ((c := sqrt(a**2 + b**2)).is_integer()) and a + b + c == p
        ]
        if len(p_sols) > largest:
            largest = p
            solutions = p_sols

    # print(f"{solutions = }")
    print(f"{largest}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
