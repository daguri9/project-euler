# Inverted sssp on DAG
def longest_path(triangle):
    path = {}
    inverted = [list(map(lambda x: -x, i)) for i in triangle]
    estimates = {(0, 0): inverted[0][0]}

    for i in range(len(inverted)-1):
        for j in range(len(inverted[i])):
            pos = (i, j)
            left = (i+1, j)
            right = (i+1, j+1)
            pos_est_l = inverted[left[0]][left[1]] + estimates[pos]
            pos_est_r = inverted[right[0]][right[1]] + estimates[pos]

            # Update estimate
            if left not in estimates or pos_est_l < estimates[left]:
                estimates[left] = pos_est_l
                path[left] = pos
            if right not in estimates or pos_est_r < estimates[right]:
                estimates[right] = pos_est_r
                path[right] = pos


    last_row_est = {pos: est for pos, est in estimates.items() if pos[0] == len(inverted)-1}
    shortest = min(last_row_est, key=last_row_est.get)
    nxt = shortest
    sol_path = [nxt]
    while nxt != (0, 0):
        nxt = path[nxt]
        sol_path.append(nxt)

    return sol_path, -estimates[shortest]

if __name__ == "__main__":
    with open('triangle.txt') as f:
        triangle = [[int(x) for x in line.rstrip('\n').split()] for line in f]

    result = longest_path(triangle)
    print(f"path = {result[0]}")
    print(f"total sum = {result[1]}")