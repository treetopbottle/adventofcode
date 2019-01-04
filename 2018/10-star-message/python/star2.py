#!/usr/bin/env python3


from collections import defaultdict


def star_print(stars, min_x, min_y, max_x, max_y):
    pixels = defaultdict(bool)
    for x, y, vx, vy in stars:
        pixels[(x, y)] = True

    for i in range(min_y, max_y+1):
        for j in range(min_x, max_x+1):
            if pixels[(j, i)]:
                print('#', end='')
            else:
                print('.', end='')
        print()


def move(stars):
    new_stars = []
    for x, y, vx, vy in stars:
        new_star = (x+vx, y+vy, vx, vy)
        new_stars.append(new_star)
    return new_stars


stars = []
min_x = int( 1e8)
max_x = int(-1e8)
min_y = int( 1e8)
max_y = int(-1e8)
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        x = int(line[10:16])
        y = int(line[18:24])
        vx = int(line[36:38])
        vy = int(line[40:42])

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        stars.append((x, y, vx, vy))

area = abs(min_x - max_x) * abs(min_y - max_y)
for i in range(1, 11000):
    stars = move(stars)
    min_x = min(stars, key=lambda x: x[0])[0]
    min_y = min(stars, key=lambda x: x[1])[1]
    max_x = max(stars, key=lambda x: x[0])[0]
    max_y = max(stars, key=lambda x: x[1])[1]
    area = abs(min_x - max_x) * abs(min_y - max_y)
    if area < 2000:
        print()
        print(i, ':')
        star_print(stars, min_x, min_y, max_x, max_y)
        import time; time.sleep(1)

