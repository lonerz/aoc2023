from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

with open('day19_input.txt') as f:
    workflows, ratings = f.read().split("\n\n")
    workflows = workflows.split()
    ratings = ratings.split()

    nodes = set()
    graph = {}
    for workflow in workflows:
        name = workflow[:workflow.index('{')]
        nodes.add(name)
        conds = workflow[workflow.index('{')+1:workflow.index('}')].split(',')
        graph[name] = conds

    START = 'in'
    def dfs(node, rating):
        if node == 'A':
            return 'A'
        elif node == 'R':
            return 'R'

        conds = graph[node]
        satisfied = False
        for cond in conds[:-1]:
            if ':' in cond:
                condition, dest = cond.split(':')
                for var in ['x', 'm', 'a', 's']:
                    condition = condition.replace(var, rating[var])
                if eval(condition):
                    return dfs(dest, rating)

        return dfs(conds[-1], rating)

    ans = 0
    for part in ratings:
        partd = {}
        partsum = 0
        for x in part[1:-1].split(','):
            var, num = x.split('=')
            partd[var] = num
            partsum += int(num)
        if dfs(START, partd) == 'A':
            ans += partsum
    print(ans)

