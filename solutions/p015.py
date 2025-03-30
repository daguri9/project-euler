from math import comb

def compute(n):
    return comb(n+n, n)

if __name__ == "__main__":
    print(compute(20))