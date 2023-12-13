with open('day4_input.txt') as f:
    lines = f.readlines()
    ans = 0
    cards = [0] * 1000000
    for card_i, l in enumerate(lines):
        a = l.strip()
        a = a.split(":")[-1]
        a = a.split("|")
        winning = a[0]
        nums = a[-1]
        winning = [int(x) for x in winning.split()]
        nums = [int(x) for x in nums.split()]
        if not winning and not nums:
            continue

        cards[card_i] += 1
        count = 0
        for x in nums:
            if x in winning:
                count += 1

        for i in range(card_i + 1, card_i + count + 1):
            cards[i] += cards[card_i]

    ans = 0
    for i in range(1000000):
        ans += cards[i]
    print(ans)


