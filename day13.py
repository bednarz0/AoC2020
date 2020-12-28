with open('day13.txt') as f:
    tstart = int(f.readline())
    line = f.readline().rstrip().split(',')

dmin = tstart
for x in line:
    if x == 'x':
        continue
    x = int(x)
    d = x - (tstart % x)

    if d < dmin:
        dmin = d
        out = d * x
print('Part 1:', out)

with open('day13.txt') as f:
    f.readline()
    line = f.readline().rstrip().split(',')

buslist = []
x = 0
for m in line:
    if m != 'x':
        buslist.append((x,int(m)))
    x += 1

step = 1
t = 0

while True:
    for x,m in buslist[:]:
        if (t + x) % m == 0:
            step *= m
            buslist.remove((x,m))
    if len(buslist) == 0:
        break
    t += step

print('Part 2:', t)