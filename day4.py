with open('day4_input.txt') as f:
    lines = f.readlines()
    ans = 0
    for l in lines:
        a = l.strip()
        a = a.split(":")[-1]
        a = a.split("|")
        winning = a[0]
        nums = a[-1]
        winning = [int(x) for x in winning.split()]
        nums = [int(x) for x in nums.split()]

        count = 0
        for x in nums:
            if x in winning:
                count += 1

        temp = 1
        for x in range(count - 1):
            temp *= 2
        if count:
            ans += temp
    print(ans)


