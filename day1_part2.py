nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('day1_input.txt') as f:
    lines = f.readlines()
    s = 0
    for l in lines:
        a = l.strip()
        first = None
        for i in range(len(a)):
            if a[i].isdigit():
                first = a[i]
                break
            found = False
            for j, n in enumerate(nums):
                if n == a[i:i+len(n)]:
                    first = str(j + 1)
                    found = True
                    break
            if found:
                break
        last = None
        for i in range(len(a)-1,-1,-1):
            if a[i].isdigit():
                last = a[i]
                break
            found = False
            for j, n in enumerate(nums):
                if n == a[i-len(n) + 1:i + 1]:
                    last = str(j + 1)
                    found = True
                    break
            if found:
                break
        s += int(first + last)
    print(s)


