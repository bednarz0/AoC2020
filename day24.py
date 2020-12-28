dxy = {'e':(2,0), 'ne':(1,1), 'se':(1,-1), 'w':(-2,0), 'nw':(-1,1), 'sw':(-1,-1)}
blktiles = set()

with open('day24.txt') as f:
    for line in f:
        dir = ''
        p = (0,0)
        for c in line.strip():
            if c in 'ns':
                dir += c
                continue
            dir += c
            p = tuple(map(lambda x,y:x+y, dxy[dir], p))
            dir = ''
        blktiles ^= {p}
print('Part 1:', len(blktiles))

def flipfloor(blktiles):
    newblktiles = set()
    blkneighbors = {}
    for (x,y) in blktiles:
        cnt = 0
        for xf,yf in [(x+2,y), (x+1,y+1), (x+1,y-1), (x-2,y), (x-1,y+1), (x-1,y-1)]:
            if (xf,yf) in blktiles:
                cnt += 1
            else:
                if (xf,yf) not in blkneighbors:
                    blkneighbors[(xf,yf)] = 0
                blkneighbors[(xf,yf)] += 1
        if cnt == 1 or cnt == 2:
            newblktiles.add((x,y))
    for (x,y), cnt in blkneighbors.items():
        if cnt == 2:
            newblktiles.add((x,y))
    return newblktiles

for _ in range(100):
    blktiles = flipfloor(blktiles)
print('Part 2:', len(blktiles))

