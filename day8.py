import math

with open('day8_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    graph = {}
    instructions = lines[0]
    for l in lines[2:]:
        a = l.split(" = ")
        x = a[0]
        left = (a[1].split(", "))[0][1:]
        right = (a[1].split(", "))[1][:-1]
        graph[x] = ((left, right))

    cur = 'AAA'
    ans = 0
    for ins in instructions * 1000:
        ans += 1
        cur = graph[cur][0 if ins == 'L' else 1]
        if cur == 'ZZZ':
            break
    print(ans)

