with open('day3_input.txt') as f:
    lines = f.readlines()
    visited = []
    grid = []
    for l in lines:
        a = l.strip()
        grid.append(list(a))
        temp = []
        for _ in range(len(grid[-1])):
            temp.append(set())
        visited.append(temp)

    gear_num = 1
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                # check surrounding
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx = i + dx
                        ny = j + dy
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                            visited[nx][ny].add(gear_num)
                gear_num += 1


    gear_to_nums = {}

    for i in range(len(grid)):
        j = 0
        while j < len(grid[0]):
            if grid[i][j].isdigit():
                number = ""
                gears = set()
                while j < len(grid[0]) and grid[i][j].isdigit():
                    if visited[i][j]: gears = gears.union(visited[i][j])
                    number += grid[i][j]
                    j += 1
                for gear in gears:
                    if gear in gear_to_nums:
                        gear_to_nums[gear].append(int(number))
                    else:
                        gear_to_nums[gear] = [int(number)]
            j += 1

    ans = 0
    for gear, nums in gear_to_nums.items():
        if len(nums) == 2:
            ans += nums[0] * nums[1]
    print(ans)

