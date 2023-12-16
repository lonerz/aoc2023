import sys
sys.setrecursionlimit(1000000)

with open('day16_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    R = len(lines)
    C = len(lines[0])

    visited = [[[0 for k in range(4)] for i in range(C)] for j in range(R)]
    drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, dr):
        if x < 0 or x >= R or y < 0 or y >= C:
            return

        if visited[x][y][dr]:
            return
        visited[x][y][dr] = 1

        c = lines[x][y]
        if c == '.':
            dfs(x + drs[dr][0], y + drs[dr][1], dr)
        if c == '/':
            d_to_d = {0: 3, 1: 2, 2: 1, 3: 0}
            new_dr = d_to_d[dr]
            dfs(x + drs[new_dr][0], y + drs[new_dr][1], new_dr)
        if c == '\\':
            d_to_d = {0: 1, 1: 0, 2: 3, 3: 2}
            new_dr = d_to_d[dr]
            dfs(x + drs[new_dr][0], y + drs[new_dr][1], new_dr)
        if c == '|':
            d_to_d = {0: [1, 3], 1: [1], 2: [1, 3], 3: [3]}
            for new_dr in d_to_d[dr]:
                dfs(x + drs[new_dr][0], y + drs[new_dr][1], new_dr)
        if c == '-':
            d_to_d = {0: [0], 1: [0, 2], 2: [2], 3: [0, 2]}
            for new_dr in d_to_d[dr]:
                dfs(x + drs[new_dr][0], y + drs[new_dr][1], new_dr)

    dfs(0, 0, 0)

    ans = 0
    for i in range(R):
        for j in range(C):
            for k in range(4):
                if visited[i][j][k]:
                    ans += 1
                    break
    print(ans)

