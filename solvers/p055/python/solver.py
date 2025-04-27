import time


def is_lychrel(n, it=0):
    if it == 51:
        return True
    elif str(n) != str(n)[::-1] or it == 0:
        return is_lychrel(n + int(str(n)[::-1]), it + 1)
    else:
        return False


def main():
    count = 0
    for i in range(1, 10_000):
        count += 1 if is_lychrel(i) else 0
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
