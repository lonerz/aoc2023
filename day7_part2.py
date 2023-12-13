import functools
from collections import Counter

def score_hand(hand):
    c = Counter(hand)
    js = c["J"]
    counts = list(sorted(c.values(), reverse=True))
    if counts == [5]: return 1
    if counts == [4, 1]: return 2 if not js else 1
    if counts == [3, 2]: return 3 if not js else 1
    if counts == [3, 1, 1]: return 4 if not js else 2
    if counts == [2, 2, 1]: return 5 if not js else (2 if js == 2 else 3)
    if counts == [2, 1, 1, 1]: return 6 if not js else 4
    if counts == [1, 1, 1, 1, 1]: return 7 if not js else 6

strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

with open('day7_input.txt') as f:
    lines = f.readlines()
    hands = []
    for l in lines:
        a = l.strip()
        hand, bid = a.split()
        bid = int(bid)
        hands.append((hand, bid, score_hand(hand)))

    def sort_func(x, y):
        if x[2] < y[2]: return 1
        if x[2] > y[2]: return -1
        for i,j in zip(x[0],y[0]):
            if strength.index(i) < strength.index(j): return 1
            if strength.index(i) > strength.index(j): return -1
        return 0

    sorted_hands = sorted(hands, key=functools.cmp_to_key(sort_func))

    ans = 0
    for i, (_, bid, _) in enumerate(sorted_hands):
        ans += bid * (i + 1)
    print(ans)

