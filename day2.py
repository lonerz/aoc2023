COLORS = {"red": 12, "green": 13, "blue": 14}

with open('day2_input.txt') as f:
    lines = f.readlines()
    ans = 0
    for game_i, l in enumerate(lines):
        a = l.strip()
        game = a.split(": ")[-1]
        sets = game.split('; ')
        not_possible = False
        for s in sets:
            colors = s.split(", ")
            for color in colors:
                num,color = color.split(" ")
                num = int(num)
                max_num = COLORS[color]
                if num > max_num:
                    not_possible = True

        if not not_possible:
            ans += game_i + 1
    print(ans)

