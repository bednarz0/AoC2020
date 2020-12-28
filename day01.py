with open('day01.txt') as f:
    nlist = [int(x) for x in f]

nlen = len(nlist)
nlist.sort()
i, j = 0, nlen-1
while True:
    t = nlist[i] + nlist[j]
    if t == 2020:
        break
    elif t < 2020:
        i += 1
    else:
        j -= 1

print('Part 1:', nlist[i]*nlist[j])

for k in range(nlen):
    i, j = k+1, nlen-1
    while i < j:
        t = nlist[i] + nlist[j] + nlist[k]
        if t == 2020:
            break
        elif t < 2020:
            i += 1
            if i == k:
                i += 1
        else:
            j -= 1
            if j == k:
                j -= 1

    if t == 2020:
        break

print('Part 2:', nlist[i]*nlist[j]*nlist[k])

