import sys
sys.setrecursionlimit(1000000)

def solve(s):
    cur = 0
    for x in s:
        cur += ord(x)
        cur *= 17
        cur %= 256
    return cur

with open('day15_input.txt') as f:
    seq = f.read().strip().split(",")

    ans = 0
    for x in seq:
        ans += solve(x)
    print(ans)

