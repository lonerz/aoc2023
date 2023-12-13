import math

with open('day8_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    graph = {}
    instructions = lines[0]
    start_nodes = set()
    end_nodes = set()
    for l in lines[2:]:
        a = l.split(" = ")
        x = a[0]
        left = (a[1].split(", "))[0][1:]
        right = (a[1].split(", "))[1][:-1]
        graph[x] = ((left, right))

        if x.endswith('A'):
            start_nodes.add(x)
        if x.endswith('Z'):
            end_nodes.add(x)

    ans = 1
    for start in start_nodes:
        cur = start
        last = None
        diff = None
        for i, ins in enumerate(instructions * 1000):
            cur = graph[cur][0 if ins == 'L' else 1]
            if cur in end_nodes:
                if last:
                    diff = i - last
                    break
                else:
                    last = i
        ans = ans * diff // math.gcd(ans, diff)

    print(ans)

