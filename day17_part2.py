from heapq import heappush, heappop
from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day17_input.txt') as f:
    lines = [[int(x) for x in l.strip()] for l in f.readlines()]

    R = len(lines)
    C = len(lines[0])

    drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # create new graph
    graph = defaultdict(list)   # v => [(v, dist)]
    for x in range(R):
        for y in range(C):
            if x == R - 1 and y == C - 1:
                continue

            for d in range(4):
                dx, dy = drs[d]
                nx, ny = x + dx, y + dy

                # if 0 <= path < 10, we have to move in that direction
                if 0 <= nx < R and 0 <= ny < C:
                    for path in range(10):
                        graph[(x, y, d, path)].append(((nx, ny, d, path + 1), lines[nx][ny]))

                # if 4 < path < 10, we can try left/right turn
                d1 = (d + 1) % 4
                d1x, d1y = drs[d1]
                n1x, n1y = x + d1x, y + d1y

                if 0 <= n1x < R and 0 <= n1y < C:
                    for path in range(4, 11):
                        graph[(x, y, d, path)].append(((n1x, n1y, d1, 1), lines[n1x][n1y]))

                d2 = (d + 3) % 4
                d2x, d2y = drs[d2]
                n2x, n2y = x + d2x, y + d2y

                if 0 <= n2x < R and 0 <= n2y < C:
                    for path in range(4, 11):
                        graph[(x, y, d, path)].append(((n2x, n2y, d2, 1), lines[n2x][n2y]))

    # START: (0, 0), 0, 0
    # END: (R - 1, C - 1), ANY, ANY

    INF = 10000000000000

    dist = defaultdict(lambda: INF)
    prev = {}
    q = []

    dist[(0, 0, 0, 0)] = 0
    dist[(0, 0, 1, 0)] = 0

    for x in range(R):
        for y in range(C):
            for d in range(4):
                for path in range(11):
                    heappush(q, (dist[(x, y, d, path)], (x, y, d, path)))

    while len(q):
        d, node = heappop(q)
        if d > dist[node]:
            continue

        for neighbor, edist in graph[node]:
            if dist[node] + edist < dist[neighbor]:
                dist[neighbor] = dist[node] + edist
                prev[neighbor] = node
                heappush(q, (dist[neighbor], neighbor))

    ans = INF
    for d in range(4):
        # start at 4 cuz the crucible can't stop if it didn't go 4 in a direction
        for path in range(4, 11):
            ans = min(ans, dist[(R - 1, C - 1, d, path)])
    print(ans)

