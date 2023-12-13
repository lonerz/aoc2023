import sys
sys.setrecursionlimit(1000000)

def test_h(g, last_h):
    for r in range(1, len(g)):
        if r == last_h:
            continue

        r1 = r - 1
        r2 = r
        works = True
        while r1 >= 0 and r2 < len(g):
            if g[r1] != g[r2]:
                works = False
            r1 -= 1
            r2 += 1
        if works:
            return r

def test_v(g, last_v):
    for c in range(1, len(g[0])):
        if c == last_v:
            continue
        c1 = c - 1
        c2 = c
        works = True
        while c1 >= 0 and c2 < len(g[0]):
            t1 = []
            for i in range(len(g)):
                t1.append(g[i][c1])
            t2 = []
            for i in range(len(g)):
                t2.append(g[i][c2])
            if t1 != t2:
                works = False
            c1 -= 1
            c2 += 1
        if works:
            return c

with open('day13_input.txt') as f:
    th = 0
    tv = 0
    graphs = f.read().split("\n\n")
    for graph in graphs:
        g = graph.strip()
        g = g.split("\n")
        g = [list(x) for x in g]

        last_h = test_h(g, -1)
        last_v = test_v(g, -1)

        found = False
        for i in range(len(g)):
            for j in range(len(g[0])):
                temp = g[i][j]
                g[i][j] = '#' if temp == '.' else '.'

                h = test_h(g, last_h)
                v = test_v(g, last_v)

                g[i][j] = temp

                if h and h != last_h:
                    found = True
                    th += h
                    break

                if v and v != last_v:
                    found = True
                    tv += v
                    break

            if found:
                break

    print(tv + th * 100)

