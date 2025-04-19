import time
import matplotlib.pyplot as plt
from math import factorial


def comput_dfs(n):
    result = sum(map(lambda x: factorial(int(x)), str(n)))
    return result


def main():
    # fig, ax = plt.subplots()
    # x = [i for i in range(100000)]
    # y = list(map(comput_dfs, x))
    # ax.plot(x, y)
    # plt.show()
    print_interval = 1000
    targets = []
    for i in range(10, 100_000):
        if i % print_interval == 0:
            print(f"Checking: {i}", end="\r")
        if comput_dfs(i) == i:
            targets.append(i)

    print()
    print(f"{targets}")
    print(f"{sum(targets)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
