import sys
sys.setrecursionlimit(1000000)

with open('day10_input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]
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
            return

        visited[x][y] = 1
        dx, dy = drs[dr][c]
        nx, ny = dx + x, dy + y
        if visited[nx][ny]:
            if nx == start[0] and ny == start[1]:
                print('ending dir', dx ,dy)
            return
        dfs((nx, ny), (dx, dy))

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        print('trial', dx, dy)
        visited[start[0]][start[1]] = 1
        dfs((start[0] + dx, start[1] + dy), (dx, dy))

    count = 0
    for i in range(R):
        count += sum(visited[i])
    print(count)

    lines[start[0]][start[1]] = 'L'  # extrapolated from trail + ending dir

    inside = 0
    for i in range(R):
        for j in range(C):
            if not visited[i][j]:
                # make ray go right, count even/odd intersections
                count = 0
                ni, nj = i, j
                last = None 
                while nj < C:
                    if visited[ni][nj]:
                        if lines[ni][nj] == '|':
                            count += 1
                        elif lines[ni][nj] == '-':
                            pass
                        else:
                            if last:
                                if (last, lines[ni][nj]) in [('L', '7'), ('F', 'J')]:
                                    count += 1
                                last = None
                            else:
                                last = lines[ni][nj]
                    nj += 1
                if count % 2:
                    inside += 1

    print(inside)

