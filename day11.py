with open('day11_input.txt') as f:
    graph = [list(l.strip()) for l in f.readlines()]
    R = len(graph)
    C = len(graph[0])

    rows = []
    cols = []
    for i in range(R):
        empty = True
        for j in range(C):
            if graph[i][j] != '.':
                empty = False
        if empty: rows.append(i)

    for i in range(C):
        empty = True
        for j in range(R):
            if graph[j][i] != '.':
                empty = False
        if empty: cols.append(i)

    g = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '#':
                g.append((i, j))

    ans = 0
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            without = abs(g[i][0] - g[j][0]) + abs(g[i][1] - g[j][1])

            mn = min(g[i][0], g[j][0])
            mx = max(g[i][0], g[j][0])
            for x in rows:
                if mn <= x <= mx:
                    without += 1

            mn = min(g[i][1], g[j][1])
            mx = max(g[i][1], g[j][1])
            for x in cols:
                if mn <= x <= mx:
                    without += 1

            ans += without

    print(ans)

