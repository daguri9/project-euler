import time


# Get repetend by long division
def rep_len(n, m):
    r = n % m
    divisors = []
    reptend = ""
    length = 0
    while r not in divisors:
        if r == 0:
            return "", 0
        length += 1
        divisors.append(r)
        reptend += str((r * 10) // m)
        r = (r * 10) % m

    rep_pos = divisors.index(r)
    reptend = reptend[rep_pos:]
    length -= rep_pos

    return reptend, length


def main():
    largest = 0
    largest_val = 0
    div = 0
    for i in range(1, 1000):
        rep, length = rep_len(1, i)
        if length > largest_val:
            largest_val = length
            largest = rep
            div = i

    print(f"Longest recurring cycle with 1/{div}")
    print(f"Repetend {largest}")
    print(f"Length {largest_val}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
