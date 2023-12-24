import sys
sys.setrecursionlimit(1073741824)

with open('day18_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ds = []
    nums = []

    straight2 = 0

    for l in lines:
        d, num, hx = l.split()
        hx = hx[1:-1]

        d = int(hx[-1])
        num = int(hx[1:-1], 16)

        nums.append(num)
        ds.append(d)

        straight2 += num - 1 if num >= 1 else 0

    corner1 = 0
    corner3 = 0

    for d1, d2 in zip(ds, ds[1:] + [ds[0]]):
        if (d1, d2) in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            corner1 += 1
        else:
            corner3 += 1

    drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    points = []
    xs = []
    ys = []

    perimeter = 0
    x = 0
    y = 0
    for d, n in zip(ds, nums):
        xs.append(x)
        ys.append(y)

        dx, dy = drs[d]
        nx, ny = x + dx * n, y + dy * n
        perimeter += abs(x - nx) + abs(y - ny)
        x, y = nx, ny

    # shoelace theorem
    area = 0
    for x, y in zip(xs[:-1], ys[1:]):
        area += x * y
    for x, y in zip(xs[1:], ys[:-1]):
        area -= x * y
    area = abs(area) // 2

    print(perimeter + (area * 4 - corner1 - 2 * straight2 - 3 * corner3) // 4)

