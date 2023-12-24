import sys
sys.setrecursionlimit(1073741824)

with open('day18_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ds = []
    nums = []

    for l in lines:
        d, num, _ = l.split()
        num = int(num)
        ds.append(d)
        nums.append(num)

    drs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

    x = 0
    y = 0
    mnx = 1000000000
    mny = 1000000000
    mxx = -1000000000
    mxy = -1000000000
    for d, n in zip(ds, nums):
        dx, dy = drs[d]
        x += dx * n 
        y += dy * n
        mnx = min(mnx, x)
        mny = min(mny, y)
        mxx = max(mxx, x)
        mxy = max(mxy, y)

    R = mxx - mnx + 10  # add some buffer
    C = mxy - mny + 10  # add some buffer
    grid = [['.' for i in range(C)] for j in range(R)]

    x = -mnx
    y = -mny

    for d, n in zip(ds, nums):
        dx, dy = drs[d]
        for _ in range(n):
            grid[x][y] = '#'
            x += dx
            y += dy

    visited = set()
    q = [(x - 2, y - 2)]  # this is for the input
    while len(q):
        x, y = q.pop(0)
        if (x, y) in visited:
            continue
        grid[x][y] = 'O'
        visited.add((x, y))
        for d in drs.values():
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.' and (nx, ny) not in visited:
                q.append((nx, ny))

    ans = 0
    for g in grid:
        for c in g:
            if c in ['#', 'O']:
                ans += 1
    print(ans)

