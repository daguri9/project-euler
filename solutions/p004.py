def compute():
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            candidate = str(i * j)
            if candidate == candidate[::-1]:
                return candidate, i, j


if __name__ == "__main__":
    print(compute())