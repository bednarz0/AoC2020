from itertools import product

def simulate(space):
    newspace = {}
    emptyspace = {}

    dim = len(list(space.keys())[0]) # grab any key from space to learn if this is 3D or 4D.
    dpzero = (0,) * dim

    for p, x in space.items():
        cnt = 0
        for dp in product((1, 0, -1), repeat=dim):
            if dp == dpzero:
                continue
            p2 = tuple(map(sum, zip(p, dp)))
            if p2 in space:
                cnt += 1
            else:
                if p2 not in emptyspace:
                    emptyspace[p2] = 0
                emptyspace[p2] += 1
        if cnt == 2 or cnt == 3:
            newspace[p] = '#'
    for p, x in emptyspace.items():
        if x == 3:
            newspace[p] = '#'
    return newspace

space3 = {}
space4 = {}

with open('day17.txt') as f:
    y = 0
    for line in f:
        for x, c in enumerate(line.strip()):
            if c == '#':
                space3[(x,y,0)] = '#'
                space4[(x,y,0,0)] = '#'
        y += 1

for _ in range(6):
    space3 = simulate(space3)
    space4 = simulate(space4)

print('Part 1:', len(space3))
print('Part 2:', len(space4))
