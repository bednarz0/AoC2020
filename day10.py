with open('day10.txt') as f:
    series = [int(x) for x in f]

series.append(0)
series.append(max(series)+3)
series.sort()

d = [0]*4
for i in range(len(series)-1):
    d[series[i+1] - series[i]] += 1

print('Part 1:', d[1]*d[3])

with open('day10.txt') as f:
    series = [int(x) for x in f]

series.sort()
target = max(series)

precompute = [None]*target
def count(t):
    if t == target:
        return 1

    if precompute[t] != None:
        return precompute[t]

    cnt = 0
    for i in [1,2,3]:
        if t+i in series:
            cnt += count(t+i)

    precompute[t] = cnt
    return cnt

print('Part 2:', count(0))
