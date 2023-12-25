from sympy import symbols, solve, And
from sympy.core.relational import Relational
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

    # probably faster to roll my own inequality checks instaed of sympy but oh well
    vrs = {'x': symbols('x'), 'm': symbols('m'), 'a': symbols('a'), 's': symbols('s')}

    START = 'in'
    def dfs(node, relations):
        if node == 'A':
            ans = solve(relations, list(vrs.values()))

            conditions = And.make_args(ans)
            highs = defaultdict(lambda: 4000)
            lows = defaultdict(lambda: 1)
            ineqst = defaultdict(list)
            for cond in conditions:
                s = str(cond)
                for vs in vrs.keys():
                    if vs in s:
                        for x in cond.atoms(Relational):
                            op = x.canonical.rel_op
                            val = x.canonical.rhs
                            if op == '<':
                                highs[vs] = val - 1
                            elif op == '<=':
                                highs[vs] = val
                            elif op == '>':
                                lows[vs] = val + 1
                            elif op == '>=':
                                lows[vs] = val

            ans = 1
            for vs in vrs.keys():
                ans *= highs[vs] - lows[vs] + 1
            return ans
        elif node == 'R':
            return 0

        sm = 0
        conds = graph[node]
        satisfied = False
        opposite = []

        for cond in conds[:-1]:
            if ':' in cond:
                condition, dest = cond.split(':')
                if '>' in condition:
                    var, num = condition.split('>')
                    sm += dfs(dest, relations + [vrs[var] > int(num)] + opposite)
                    opposite.append(vrs[var] <= int(num))
                elif '<' in condition:
                    var, num = condition.split('<')
                    sm += dfs(dest, relations + [vrs[var] < int(num)] + opposite)
                    opposite.append(vrs[var] >= int(num))

        # the fallback case
        return sm + dfs(conds[-1], relations + opposite)

    start = []
    for sym in vrs.values():
        start.append(sym >= 1)
        start.append(sym <= 4000)
    print(dfs(START, start))

