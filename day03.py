x = 0
treecnt = 0

with open('day03.txt') as f:
    for line in f:
        line = line.strip()
        if line[x % len(line)] == '#':
            treecnt += 1
        x += 3
print('Part 1:', treecnt)

treeprod = 1
for (dx,dy) in zip([1,3,5,7,1], [1,1,1,1,2]):
    x, y = 0, 0
    treecnt = 0

    with open('day03.txt') as f:
        for line in f:
            if y % dy == 0:
                line = line.strip()
                if line[x % len(line)] == '#':
                    treecnt += 1
                x += dx
            y += 1

    treeprod *= treecnt
print('Part 2:', treeprod)




