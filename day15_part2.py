import sys
sys.setrecursionlimit(1000000)

def hash(s):
    cur = 0
    for x in s:
        cur += ord(x)
        cur *= 17
        cur %= 256
    return cur

boxes = []
for i in range(256):
    boxes.append([])

with open('day15_input.txt') as f:
    seq = f.read().strip().split(",")

    for x in seq:
        label = None
        if "=" in x:
            label = x[:-2]
            h = hash(label)
            val = int(x[-1])
            added = False
            for i,slot in enumerate(boxes[h]):
                if slot[0] == label:
                    boxes[h][i][1] = val
                    added = True
            if not added:
                boxes[h].append([label, val])
        if "-" in x:
            label = x[:-1]
            h = hash(label)
            for i,slot in enumerate(boxes[h]):
                if slot[0] == label:
                    boxes[h].pop(i)
                    break

    ans = 0
    for i, slots in enumerate(boxes):
        for j, slot in enumerate(slots):
            ans += (i + 1) * (j + 1) * slot[1]
    print(ans)


