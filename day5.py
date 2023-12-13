with open('day5_input.txt') as f:
    lines = f.readlines()

    input_i = 0
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humidity = []
    humidity_to_location = []

    for l in lines:
        a = l.strip()
        if not a:
            input_i += 1
            continue

        if input_i == 0:
            seeds = [int(x) for x in a.split("seeds: ")[-1].split(" ")]

        elif input_i == 1:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            seed_to_soil.append(tuple(a))

        elif input_i == 2:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            soil_to_fertilizer.append(tuple(a))

        elif input_i == 3:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            fertilizer_to_water.append(tuple(a))

        elif input_i == 4:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            water_to_light.append(tuple(a))

        elif input_i == 5:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            light_to_temp.append(tuple(a))

        elif input_i == 6:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            temp_to_humidity.append(tuple(a))

        elif input_i == 7:
            if not a[0].isdigit():
                continue
            a = [int(x) for x in a.split(" ")]
            humidity_to_location.append(tuple(a))

    ans = 1000000000000000

    for seed_i in seeds:
        soil_i = seed_i
        for end, start, r in seed_to_soil:
            if seed_i in range(start, start + r):
                soil_i = (seed_i - start) + end
                break

        f_i = soil_i
        for end, start, r in soil_to_fertilizer:
            if soil_i in range(start, start + r):
                f_i = (soil_i - start) + end
                break

        w_i = f_i
        for end, start, r in fertilizer_to_water:
            if f_i in range(start, start + r):
                w_i = (f_i - start) + end
                break

        w_i = f_i
        for end, start, r in fertilizer_to_water:
            if f_i in range(start, start + r):
                w_i = (f_i - start) + end
                break

        l_i = w_i
        for end, start, r in water_to_light:
            if w_i in range(start, start + r):
                l_i = (w_i - start) + end
                break

        t_i = l_i
        for end, start, r in light_to_temp:
            if l_i in range(start, start + r):
                t_i = (l_i - start) + end
                break

        h_i = t_i
        for end, start, r in temp_to_humidity:
            if t_i in range(start, start + r):
                h_i = (t_i - start) + end
                break

        lo_i = h_i
        for end, start, r in humidity_to_location:
            if h_i in range(start, start + r):
                lo_i = (h_i - start) + end
                break

        ans = min(ans, lo_i)

    print(ans)


