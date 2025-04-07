def compute():
    candidates = [(a, b, c) for a in range(1, 1000) for b in range(1, 1000) for c in range(1, 1000) if c > b and b > a and a + b + c == 1000 and a**2 + b**2 == c**2][0]
    print(f"{candidates = }")
    return candidates[0] * candidates[1] * candidates[2]

if __name__ == "__main__":
    print(compute())