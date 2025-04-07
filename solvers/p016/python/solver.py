def compute():
    digits = list(str(2**1000))
    result = 0
    for d in digits:
        result += int(d)

    return result

if __name__ == "__main__":
    print(compute())