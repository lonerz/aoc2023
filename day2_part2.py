with open('day2_input.txt') as f:
    lines = f.readlines()
    ans = 0
    for game_i,l in enumerate(lines):
        MIN_COLORS = {"red": 0, "green": 0, "blue": 0}
        a = l.strip()
        game = a.split(": ")[-1]
        sets = game.split('; ')
        not_possible = False
        for s in sets:
            colors = s.split(", ")
            for color in colors:
                num,color = color.split(" ")
                num = int(num)
                MIN_COLORS[color] = max(MIN_COLORS[color], num)

        ans += MIN_COLORS["red"] * MIN_COLORS["green"] * MIN_COLORS["blue"]
    print(ans)

