d = 1
x, y = 0, 0

dx = {0:0, 1:1, 2:0, 3:-1}
dy = {0:1, 1:0, 2:-1, 3:0}

with open('day12.txt') as f:
    for line in f:
        value = int(line[1:].rstrip())

        if line[0] == 'N':
            y += value
        elif line[0] == 'E':
            x += value
        elif line[0] == 'S':
            y -= value
        elif line[0] == 'W':
            x -= value
        elif line[0] == 'F':
            x += dx[d]*value
            y += dy[d]*value
        elif line[0] == 'R':
            d = (d + (value//90)) % 4
        elif line[0] == 'L':
            d = (d - (value//90)) % 4

print('Part 1:', abs(x) + abs(y))

wx, wy = 10, 1
sx, sy = 0, 0

with open('day12.txt') as f:
    for line in f:
        value = int(line[1:].rstrip())

        if line[0] == 'N':
            wy += value
        elif line[0] == 'E':
            wx += value
        elif line[0] == 'S':
            wy -= value
        elif line[0] == 'W':
            wx -= value
        elif line[0] == 'F':
            sx += wx*value
            sy += wy*value
        else:
            if (line[0] == 'L' and value == 90) or (line[0] == 'R' and value == 270):
                wx, wy = -wy, wx
            elif value == 180:
                wx, wy = -wx, -wy
            else:
                wx, wy = wy, -wx

print('Part 2:', abs(sx) + abs(sy))
