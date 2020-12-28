mem = {}

with open('day14.txt') as f:
    for line in f:
        line = line.rstrip().split(' ')

        if line[0] == 'mask':
            maskX, mask1 = 0, 0
            for c in line[2].rstrip():
                maskX, mask1 = maskX << 1, mask1 << 1
                if c == 'X':
                    maskX |= 1
                elif c == '1':
                    mask1 |= 1
            continue

        addr = line[0].replace('[', ' ').replace(']', ' ').split(' ')
        addr = int(addr[1])
        mem[addr] = (int(line[2]) & maskX) | mask1

print('Part 1:', sum([x for _,x in mem.items()]))

mem.clear()

with open('day14.txt') as f:
    for line in f:
        line = line.rstrip().split(' ')

        if line[0] == 'mask':
            mask = line[2].rstrip()
            xCnt = mask.count('X')

            maskX, mask1 = 0, 0
            for c in mask:
                maskX, mask1 = maskX << 1, mask1 << 1
                if c == 'X':
                    maskX |= 1
                if c == '1':
                    mask1 |= 1
            continue

        addr = line[0].replace('[', ' ').replace(']', ' ').split(' ')
        addr = (int(addr[1]) & ~maskX) | mask1
        val = int(line[2])

        for x in range(1 << xCnt):
            maskf = 0
            for c in mask:
                maskf <<= 1
                if c == 'X':
                    maskf |= x & 1
                    x >>= 1
            mem[addr | maskf] = val

print('Part 2:', sum([x for _,x in mem.items()]))