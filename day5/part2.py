import sys
import math

def solve(file):
    data = open(file, 'r').readlines()

    seed_soil   = []
    soil_fert   = []
    fert_water  = []
    water_light = []
    light_temp  = []
    temp_hum    = []
    hum_loc     = []
    conversions = []

    seeds = list(map(int, data[0].strip().split(': ')[1].split()))

    rs = []
    for i in range(0, len(seeds), 2):
        # Approximation
        for j in range(seeds[i], seeds[i] + seeds[i + 1], max(1, int(math.sqrt(seeds[i + 1]) / 25))):
            rs.append(j)

    
    i = 3
    (i, seed_soil)   = buildRange(data, i, seed_soil)
    (i, soil_fert)   = buildRange(data, i, soil_fert)
    (i, fert_water)  = buildRange(data, i, fert_water)
    (i, water_light) = buildRange(data, i, water_light)
    (i, light_temp)  = buildRange(data, i, light_temp)
    (i, temp_hum)    = buildRange(data, i, temp_hum)
    (i, hum_loc)     = buildRange(data, i, hum_loc)

    conversions = convert(seed_soil, rs)
    conversions = convert(soil_fert, conversions)
    conversions = convert(fert_water, conversions)
    conversions = convert(water_light, conversions)
    conversions = convert(light_temp, conversions)
    conversions = convert(temp_hum, conversions)
    conversions = convert(hum_loc, conversions)
    print(min(conversions))

def convert(rtab, conversions):
    for (i, val) in enumerate(conversions):
        for line in rtab:
            if val in range(line[1], line[1] + line[2]):
                val = line[0] + val - line[1]
                break
        conversions[i] = val
    return conversions

def buildRange(data, i, rtab):
    while i < len(data) and data[i] != '\n':
        rtab.append(list(map(int, data[i].split())))
        i += 1
    i += 2
    return (i, rtab)
        
    
solve(sys.argv[1])