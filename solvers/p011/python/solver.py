import time


def main():
    with open("grid.txt") as f:
        grid = [[int(x) for x in line.rstrip("\n").split()] for line in f]

    highest = 0
    for i in range(20):
        for j in range(20):
            # Horizontally
            if j <= 20 - 4:
                result = 1
                for n in grid[i][j : j + 4]:
                    result *= n
                highest = result if result > highest else highest

            # Vertically
            if i <= 20 - 4:
                result = 1
                for n in grid[i : i + 4]:
                    result *= n[j]
                highest = result if result > highest else highest

            # Diagonally downwards
            if j <= 20 - 4 and i <= 20 - 4:
                result = 1
                m = j
                for n in grid[i : i + 4]:
                    result *= n[m]
                    m += 1
                highest = result if result > highest else highest

            # Diagonally upwards
            if j <= 20 - 4 and i >= 3:
                result = 1
                m = j
                for n in grid[i : i + 4]:
                    result *= n[m]
                    m -= 1
                highest = result if result > highest else highest

    print(highest)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
