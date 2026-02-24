

arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

arrivals.sort()
departures.sort()

i = 0
j = 0

platform_need = 0
max_platform = 0

while i < len(arrivals) and j <len(departures):
    if arrivals[i] <= departures[j]:
        platform_need += 1
        i += 1

    else:
        platform_need -= 1
        j += 1
    max_platform = max(max_platform,platform_need)

print(max_platform)

