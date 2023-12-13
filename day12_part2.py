import copy

with open('day12_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    def solve(record, broke, spos, bpos, curblock, cache):
        if (spos, bpos, curblock) in cache:
            return cache[(spos, bpos, curblock)]

        if spos == len(record):
            if bpos == len(broke) and not curblock:
                return 1
            return 0

        temp = 0
        if record[spos] == '#' or record[spos] == '?':
            if bpos < len(broke) and curblock < broke[bpos]:
                temp += solve(record, broke, spos + 1, bpos, curblock + 1, cache)

        if record[spos] == '.' or record[spos] == '?':
            if curblock and bpos < len(broke) and curblock == broke[bpos]:
                temp += solve(record, broke, spos + 1, bpos + 1, 0, cache)
            elif not curblock:
                temp += solve(record, broke, spos + 1, bpos, 0, cache)

        cache[(spos, bpos, curblock)] = temp
        return temp

    ans = 0
    for l in lines:
        record, y = l.split(" ")
        record = '?'.join([record] * 5) + '.'
        broke = [int(x) for x in y.split(",")] * 5

        if '?' not in record:
            continue

        cache = {}
        temp = solve(record, broke, 0, 0, 0, cache)
        ans += temp

    print(ans)


