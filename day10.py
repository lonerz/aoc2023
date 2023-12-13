import sys
sys.setrecursionlimit(1000000)

with open('day10_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    R, C = len(lines), len(lines[0])

    start = None
    for i in range(R):
        for j in range(C):
            if lines[i][j] == 'S':
                start = (i, j)
                break

    visited = []
    for i in range(R):
        a = [0] * C
        visited.append(a)

    drs = {
        (1, 0): {'|': (1, 0), 'L': (0, 1), 'J': (0, -1)},
        (-1, 0): {'|': (-1, 0), 'F': (0, 1), '7': (0, -1)},
        (0, 1): {'-': (0, 1), '7': (1, 0), 'J': (-1, 0)},
        (0, -1): {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)},
    }
    def dfs(p, dr):
        (x, y) = p
        c = lines[x][y]
        if c not in drs[dr]:
            return 0

        visited[x][y] = 1
        dx, dy = drs[dr][c]
        nx, ny = dx + x, dy + y
        if visited[nx][ny]:
            return 1
        return dfs((nx, ny), (dx, dy)) + 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        visited[start[0]][start[1]] = 1
        dfs((start[0] + dx, start[1] + dy), (dx, dy))

    count = 0
    for i in range(R):
        count += sum(visited[i])
    print(count)

