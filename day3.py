with open('day3_input.txt') as f:
    lines = f.readlines()
    visited = []
    grid = []
    for l in lines:
        a = l.strip()
        grid.append(list(a))
        visited.append([0] * len(grid[-1]))

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j].isdigit() and grid[i][j] != ".":
                # check surrounding
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx = i + dx
                        ny = j + dy
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                            visited[nx][ny] = 1


    for i in range(len(grid)):
        j = 0
        while j < len(grid[0]):
            if grid[i][j].isdigit():
                number = ""
                visits = False
                while j < len(grid[0]) and grid[i][j].isdigit():
                    if visited[i][j]: visits = True
                    number += grid[i][j]
                    j += 1
                if visits:
                    ans += int(number)
            j += 1
    print(ans)


