import sys
sys.setrecursionlimit(1000000)

with open('day14_input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]
    ans = 0
    for i in range(len(lines[0])):
        load = len(lines)
        count = 0
        for j in range(len(lines)):
            if lines[j][i] == '#':
                count = 0
                load = len(lines) - j - 1
            if lines[j][i] == 'O':
                temp = load - count
                ans += temp
                count += 1
    print(ans)

