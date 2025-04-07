def compute(n):
    candidate = n
    while True:
        discard = False
        for i in range(1, n+1):
            if candidate % i != 0:
                discard = True
                break
        if discard:
            candidate += 1
        else:
            return candidate


if __name__ == "__main__":
    print(compute(20))