import time


def coin_combs(n, coins):
    if len(coins) == 1:
        return 1
    else:
        count = 0
        for i in range(len(coins)):
            if i == 0:
                count += 1
                continue
            for j in range(1, n // coins[i] + 1):
                remain = n - coins[i] * j
                count += coin_combs(remain, coins[:i])
        return count


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(f"{coin_combs(200, coins)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
