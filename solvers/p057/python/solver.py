import time
from fractions import Fraction


def compute(n):
    def comp(n):
        if n == 1:
            return Fraction(1, 2)
        else:
            return Fraction(1, 2 + comp(n - 1))

    return 1 + comp(n)


def main():
    count = 0
    frac = Fraction(1, 2)
    for _ in range(1_000):
        num = str((1 + frac).numerator)
        den = str((1 + frac).denominator)
        if len(num) > len(den):
            count += 1
        frac = Fraction(1, 2 + frac)
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
