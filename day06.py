def groupor(group):
    if len(group) == 0:
        return 0
    p = set([c for c in group[0]])
    for l in group[1:]:
        p = p | set([c for c in l])
    return len(p)

def groupand(group):
    if len(group) == 0:
        return 0
    p = set([c for c in group[0]])
    for l in group[1:]:
        p = p & set([c for c in l])
    return len(p)


group = []
t1, t2 = 0, 0
with open('day06.txt') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            t1 += groupor(group)
            t2 += groupand(group)
            group.clear()

        else:
            group.append(line)

t1 += groupor(group)
print('Part 1:', t1)

t2 += groupand(group)
print('Part 2:', t2)