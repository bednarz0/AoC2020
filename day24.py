dxy = {'e': (2, 0), 'ne': (1, 1), 'se': (1, -1), 'w': (-2, 0), 'nw': (-1, 1), 'sw': (-1, -1)}
btiles = set()      # set of coordinates for all black tiles

with open('day24.txt') as f:
    for line in f:
        d, p = '', (0, 0)
        for c in line.strip():
            d += c
            if c in 'ns':
                continue
            p = tuple(map(lambda x, y: x+y, dxy[d], p))
            d = ''
        btiles ^= {p}
print('Part 1:', len(btiles))


def flipfloor(btiles0):       # set of current black tiles
    btiles1 = set()           # new set of black tiles after one round
    wtiles = {}               # white tiles with black neighbors, count of black neighbors
    for p in btiles0:
        cnt = 0
        for dp in [tuple(map(lambda a, b: a+b, p, q)) for q in dxy.values()]:
            if dp in btiles0:
                cnt += 1
            else:
                if dp not in wtiles:
                    wtiles[dp] = 0
                wtiles[dp] += 1
        if cnt == 1 or cnt == 2:
            btiles1.add(p)
    for p, cnt in wtiles.items():
        if cnt == 2:
            btiles1.add(p)
    return btiles1


for _ in range(100):
    btiles = flipfloor(btiles)
print('Part 2:', len(btiles))
