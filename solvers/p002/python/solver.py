import time


def fibonacci(x: int):
    if x == 0:
        return []
    elif x == 1:
        return [1]
    l = [1, 2]
    while True:
        i = l[-1] + l[-2]
        if i <= x:
            l.append(i)
        else:
            break
    return l


def main():
    print(sum([x for x in fibonacci(4000000) if x % 2 == 0]))


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
