with open('day6_input.txt') as f:
    lines = f.readlines()
    times = int(''.join([time for time in lines[0].split(":")[-1].split()]))
    distance = int(''.join([dist for dist in lines[1].split(":")[-1].split()]))

    ans = 1
    count = 0
    for hold in range(times + 1):
        dist = hold * (times - hold)
        if dist > distance:
            count += 1
    ans *= count
    print(ans)


