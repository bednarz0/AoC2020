from itertools import product
import math

def flipImage(image): # assume all square images
    size = len(image)
    return [[image[size-1-y][x] for x in range(size)] for y in range(size)]

def rotateImage(image):
    size = len(image)
    return [[image[x][size-1-y] for x in range(size)] for y in range(size)]

class Image:
    def __init__(self, pixels):
        size = len(pixels)
        self.pixels = pixels
        self.n = ''.join([pixels[0][i] for i in range(size)])
        self.e = ''.join([pixels[i][size-1] for i in range(size)])
        self.s = ''.join([pixels[size-1][i] for i in range(size)])
        self.w = ''.join([pixels[i][0] for i in range(size)])

class Tile:
    def __init__(self, num):
        self.num = num
        self.images = []
        self.image = None

tileHeap = []
picture = {}

def placeTile(x, y, size):
    if len(tileHeap) == 0:
        return True
    for _ in range(len(tileHeap)):
        tile = tileHeap.pop(0)
        for image in tile.images:
            if x > 0 and image.w != picture[(x-1,y)].image.e:
                continue
            if y > 0 and image.n != picture[(x,y-1)].image.s:
                continue
            tile.image = image
            picture[(x,y)] = tile
            if placeTile((x+1)%size, y+(x+1)//size, size):
                return True
        tileHeap.append(tile)
    return False

with open('day20.txt') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        if not line.startswith('Tile'):
            continue

        line = line.strip().split(' ')
        tile = Tile(int(line[1].rstrip(':')))

        pixels = []
        for _ in range(10):
            pixels.append(list(file.readline().strip()))

        tile.images.append(Image(pixels))  # Generate the 8 orientations of each image
        for _ in range(3):
            tile.images.append(Image(rotateImage(tile.images[-1].pixels)))
        tile.images.append(Image(flipImage(tile.images[-1].pixels)))
        for _ in range(3):
            tile.images.append(Image(rotateImage(tile.images[-1].pixels)))

        tileHeap.append(tile)

psize = math.isqrt(len(tileHeap))
placeTile(0,0,psize)

print('Part 1:', picture[(0,0)].num * picture[(psize-1,0)].num * picture[(0,psize-1)].num * picture[(psize-1,psize-1)].num)

def findMonster(q):
    cnt = 0
    for x,y in product(range(psize*8), repeat=2):
        for dx,dy in monster:
            xf, yf = x+dx, y+dy
            if xf < 0 or xf >= 8*psize or yf < 0 or yf >= 8*psize:
                break
            if q[yf][xf] != '#':
                break
        else:
            cnt += 1
            for dx,dy in monster:
                xf, yf = x+dx, y+dy
                q[yf][xf] = 'O'
    return cnt

monster = [(0,0),(-1,0),(-1,-1),(-2,0),(-3,1),(-6,1),(-7,0),(-8,0),(-9,1),(-12,1),(-13,0),(-14,0),(-15,1),(-18,1),(-19,0)]

q = [[picture[(x//8,y//8)].image.pixels[1+y%8][1+x%8] for x in range(psize*8)] for y in range(psize*8)]
findMonster(q)
for _ in range(3):
    q = rotateImage(q)
    findMonster(q)
q = flipImage(q)
findMonster(q)
for _ in range(3):
    q = rotateImage(q)
    findMonster(q)

wavecnt = 0
for x,y in product(range(psize*8), repeat=2):
    if q[y][x] == '#':
        wavecnt += 1
print('Part 2:', wavecnt)





