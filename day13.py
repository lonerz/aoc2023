import sys
sys.setrecursionlimit(1000000)

def test_h(g):
    for r in range(1, len(g)):
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

def test_v(g):
    for c in range(1, len(g[0])):
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

        h = test_h(g)
        v = test_v(g)

        if h:
            th += h

        if v:
            tv += v

    print(tv + th * 100)

