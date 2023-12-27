import networkx as nx
from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day25_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    nodes = set()
    G = nx.DiGraph()
    for l in lines:
        src, dests = l.split(": ")
        for dest in dests.split():
            G.add_edge(src, dest, capacity=1.0)
            G.add_edge(dest, src, capacity=1.0)
            nodes.add(dest)
        nodes.add(src)

    for x in nodes:
        for y in nodes:
            if x == y: continue
            cut_value, partition = nx.minimum_cut(G, x, y)
            if cut_value == 3:
                print(len(partition[0]) * len(partition[1]))



