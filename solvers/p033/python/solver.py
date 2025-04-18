from fractions import Fraction
import time


def main():
    candidates = [
        (a, b)
        for a in range(10, 100)
        for b in range(10, 100)
        if a < b and a % 10 != 0 and b % 10 != 0 and len(set(str(a)) - set(str(b))) >= 1
    ]
    valid_fracs = []
    for i in candidates:
        a, b = i
        a_str = str(a)
        b_str = str(b)
        # try first digitz
        d = a_str[0]
        a_i = a_str.find(d)
        b_i = b_str.find(d)
        num = int(a_str[:a_i] + a_str[a_i + 1 :])
        den = int(b_str[:b_i] + b_str[b_i + 1 :])
        if num / den == a / b:
            valid_fracs.append(i)

        # try second digit
        d = a_str[1]
        a_i = a_str.find(d)
        b_i = b_str.find(d)
        num = int(a_str[:a_i] + a_str[a_i + 1 :])
        den = int(b_str[:b_i] + b_str[b_i + 1 :])
        if num / den == a / b:
            valid_fracs.append(i)

    # print(f"{valid_fracs}")
    result = 1
    for i in valid_fracs:
        result *= Fraction(i[0], i[1])
    print(f"{result.denominator}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
