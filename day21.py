import sys
from collections import defaultdict
sys.setrecursionlimit(1073741824)

with open('day21_input.txt') as f:
    grid = [list(l.strip()) for l in f.readlines()]
    R = len(grid)
    C = len(grid[0])

    start = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start = (i, j)

    INF = 10000000000
    visited = defaultdict(lambda: INF)
    q = [(start[0], start[1], 0)]
    while len(q):
        x, y, l = q.pop(0)

        if l > 64: continue
        if visited[(x, y)] != INF: continue
        visited[(x, y)] = l

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#':
                q.append((nx, ny, l + 1))

    ans = 0
    for i in range(R):
        for j in range(C):
            if visited[(i, j)] != INF and visited[(i, j)] % 2 == 0:
                ans += 1
    print(ans)

