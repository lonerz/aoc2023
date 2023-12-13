import copy

with open('day12_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    def works(r, b):
        temp = []
        cur = 0
        for x in r:
            if x == '#':
                cur += 1
            else:
                if cur:
                    temp.append(cur)
                cur = 0
        if cur:
            temp.append(cur)
        return b == temp

    def solve(r, b):
        qs = []
        for i, x in enumerate(r):
            if x == '?':
                qs.append(i)

        if len(qs) == 0:
            return 1 if works(r, b) else 0

        ans = 0
        for t in range(2 ** len(qs)):
            p = t
            ti = 0
            while p or ti < len(qs):
                if p % 2:
                    r[qs[ti]] = '#'
                else:
                    r[qs[ti]] = '.'
                p //= 2
                ti += 1
            if works(r, b):
                ans += 1

        return ans

    ans = 0
    for l in lines:
        record, y = l.split(" ")
        record = list(record)
        broke = [int(x) for x in y.split(",")]
        ans += (solve(record, broke))
    print(ans)


