map1 = []
map2 = []
m1, m2 = map1, map2

with open('day11.txt') as f:
    ymax = 0
    for line in f:
        line = line.rstrip()
        m1.append(list(line))
        ymax += 1
    xmax = len(m1[0])
m2 = [['.' for _ in range(xmax)] for _ in range(ymax)]

change, steps = True, 0
while change:
    change = False
    steps += 1

    for x in range(xmax):
        for y in range(ymax):
            if m1[y][x] == '.':
                m2[y][x] = '.'
                continue

            cnt = 0
            for x2,y2 in [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1)]:
                if x2 < 0 or y2 < 0 or x2 == xmax or y2 == ymax:
                    continue
                if m1[y2][x2] == '#':
                    cnt += 1

            if m1[y][x] == 'L':
                if cnt == 0:
                    m2[y][x] = '#'
                    change = True
                else:
                    m2[y][x] = 'L'
            elif m1[y][x] == '#':
                if cnt >= 4:
                    m2[y][x] = 'L'
                    change = True
                else:
                    m2[y][x] = '#'

    m1, m2 = m2, m1

cnt = 0
for x in range(xmax):
    for y in range(ymax):
        if m1[y][x] == '#':
            cnt += 1
print('Part 1:', cnt, 'in', steps, 'steps')

# Part 2


map1 = []
map2 = []
m1, m2 = map1, map2

with open('day11.txt') as f:
    ymax = 0
    for line in f:
        line = line.rstrip()
        m1.append(list(line))
        ymax += 1
    xmax = len(m1[0])
m2 = [['.' for _ in range(xmax)] for _ in range(ymax)]

change, steps = True, 0
while change:
    change = False
    steps += 1

    for x in range(xmax):
        for y in range(ymax):
            if m1[y][x] == '.':
                m2[y][x] = '.'
                continue

            cnt = 0
            for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                x2, y2 = x, y
                while True:
                    x2 += dx
                    y2 += dy
                    if x2 < 0 or y2 < 0 or x2 == xmax or y2 == ymax:
                        break
                    if m1[y2][x2] == '#':
                        cnt += 1
                        break
                    if m1[y2][x2] == 'L':
                        break

            if m1[y][x] == 'L':
                if cnt == 0:
                    m2[y][x] = '#'
                    change = True
                else:
                    m2[y][x] = 'L'
            elif m1[y][x] == '#':
                if cnt >= 5:
                    m2[y][x] = 'L'
                    change = True
                else:
                    m2[y][x] = '#'

    m1, m2 = m2, m1

cnt = 0
for x in range(xmax):
    for y in range(ymax):
        if m1[y][x] == '#':
            cnt += 1
print('Part 2:', cnt, 'in', steps, 'steps')


