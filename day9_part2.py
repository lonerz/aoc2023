with open('day9_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    def solve(a):
        diffs = [a]
        while True:
            last = diffs[-1]
            cur = []
            for i in range(len(last) - 1):
                cur.append(last[i + 1] - last[i])
            diffs.append(cur)
            if all([x == 0 for x in cur]):
                break
        lasts = [0]
        for i in range(len(diffs) - 2, -1 ,-1):
            lasts.append(diffs[i][0] - lasts[-1])
        return lasts[-1]

    ans = 0
    for l in lines:
        a = [int(x) for x in l.split()]
        ans += solve(a)
    print(ans)


