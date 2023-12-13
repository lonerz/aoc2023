with open('day6_input.txt') as f:
    lines = f.readlines()
    times = [int(time) for time in lines[0].split(":")[-1].split()]
    distance = [int(dist) for dist in lines[1].split(":")[-1].split()]

    ans = 1
    for i in range(len(times)):
        count = 0
        for hold in range(times[i] + 1):
            dist = hold * (times[i] - hold)
            if dist > distance[i]:
                count += 1
        ans *= count
    print(ans)

