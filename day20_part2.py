from collections import defaultdict
import sys
import math
sys.setrecursionlimit(1073741824)

with open('day20_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    graph = defaultdict(list)
    inverse_graph = defaultdict(list)
    module = {}
    for l in lines:
        name, dests = l.split(' -> ')
        dests = dests.split(", ")
        if name != 'broadcaster':
            module[name[1:]] = name[0]
            name = name[1:]
        graph[name] = dests
        for dest in dests:
            inverse_graph[dest].append(name)

    '''
    print graph to graphviz, see 4 disjoint connected modules
    for src in graph:
        for dest in graph[src]:
            print(src, '->', dest)
    '''

    ff = defaultdict(lambda: False)
    states = defaultdict(lambda: defaultdict(lambda: False))
    
    END = 'rx'
    SINKS = ['pv', 'qh', 'xm', 'hz']  # from the graphviz, find the 4 nodes that "matter"

    def lcm(x, y):
        return x * y // math.gcd(x, y)
    print(lcm(lcm(lcm(3761, 3931), 4049), 4079))  # this is the answer

    low = 0
    high = 0
    for _ in range(10 ** 6):
        start = 'broadcaster'
        q = [(start, False, start)]
        while len(q):
            node, pulse, prev = q.pop(0)
            if pulse: high += 1
            else: low += 1

            # if we have a node that matters and pulse LOW, print it out to get the cycle length
            if node in SINKS and not pulse:
                print(_, node, pulse)

            if node == start:
                for dest in graph[node]:
                    q.append((dest, pulse, node))
                continue

            if node not in module:
                continue

            mode = module[node]
            if mode == '%':
                if pulse:
                    continue
                for dest in graph[node]:
                    q.append((dest, not pulse if not ff[node] else pulse, node))
                ff[node] = not ff[node]

            elif mode == '&':
                states[node][prev] = pulse
                all_high = True
                for in_ in inverse_graph[node]:
                    if not states[node][in_]:
                        all_high = False
                for dest in graph[node]:
                    q.append((dest, False if all_high else True, node))

    print(low * high)

