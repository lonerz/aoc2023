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

    # not inclusive of the end
    seed_intervals = []
    for i in range(0, len(seeds), 2):
        seed_intervals.append((seeds[i], seeds[i] + seeds[i + 1]))
    seed_intervals.sort()

    ans = 1000000000000000

    seed_to_soil_intervals = []
    for end, start, r in seed_to_soil:
        seed_to_soil_intervals.append(((start, start + r), end - start))
    seed_to_soil_intervals.sort()

    soil_to_fertilizer_intervals = []
    for end, start, r in soil_to_fertilizer:
        soil_to_fertilizer_intervals.append(((start, start + r), end - start))
    soil_to_fertilizer_intervals.sort()

    fertilizer_to_water_intervals = []
    for end, start, r in fertilizer_to_water:
        fertilizer_to_water_intervals.append(((start, start + r), end - start))
    fertilizer_to_water_intervals.sort()

    water_to_light_intervals = []
    for end, start, r in water_to_light:
        water_to_light_intervals.append(((start, start + r), end - start))
    water_to_light_intervals.sort()

    light_to_temp_intervals = []
    for end, start, r in light_to_temp:
        light_to_temp_intervals.append(((start, start + r), end - start))
    light_to_temp_intervals.sort()

    temp_to_humidity_intervals = []
    for end, start, r in temp_to_humidity:
        temp_to_humidity_intervals.append(((start, start + r), end - start))
    temp_to_humidity_intervals.sort()

    humidity_to_location_intervals = []
    for end, start, r in humidity_to_location:
        humidity_to_location_intervals.append(((start, start + r), end - start))
    humidity_to_location_intervals.sort()

    mappings = [
        seed_to_soil_intervals,
        soil_to_fertilizer_intervals,
        fertilizer_to_water_intervals,
        water_to_light_intervals,
        light_to_temp_intervals,
        temp_to_humidity_intervals,
        humidity_to_location_intervals,
    ]
    
    def intersect(inv1, inv2):
        return inv1[0] <= inv2[1] and inv2[0] <= inv1[1]
    
    def overlap(inv1, inv2):
        return (max(inv1[0], inv2[0]), min(inv1[1], inv2[1]))

    def dfs(source_interval, mapping_i):
        if mapping_i == len(mappings):
            return source_interval[0]

        mapping = mappings[mapping_i]
        destinations = []
        for possible_interval, diff in mapping:
            if intersect(source_interval, possible_interval):
                overlap_interval = overlap(source_interval, possible_interval)
                overlap_dest = (overlap_interval[0] + diff, overlap_interval[1] + diff)
                destinations.append((overlap_interval, overlap_dest))
        
        # check for 1-to-1 mapping case
        holes = []
        if destinations:
            if source_interval[0] != destinations[0][0][0]:
                intv = (source_interval[0], destinations[0][0][0])
                holes.append((intv, intv))
            for i in range(1, len(destinations)):
                if destinations[i - 1][0][1] != destinations[i][0][0]:
                    intv = (destinations[i - 1][0][1], destinations[i][0][0])
                    holes.append((intv, intv))
            if destinations[-1][0][1] != source_interval[-1]:
                intv = (destinations[-1][0][1], source_interval[-1])
                holes.append((intv, intv))
        else:
            holes.append((source_interval, source_interval))
        destinations += holes
        destinations.sort()

        mn = 1000000000000000
        for _, destination in destinations:
            mn = min(mn, dfs(destination, mapping_i + 1))
        return mn

    for seed_interval in seed_intervals:
        ans = min(ans, dfs(seed_interval, 0))

    print(ans)

