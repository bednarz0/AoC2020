valid = [False] * 1000  # observe that all valid values are less than 1000
sum = 0

with open('day16.txt') as file:
    for line in file:
        if line == '\n':
            break

        line = line.split(':')
        vals = line[1].strip().replace('-',' ').split(' ')
        for x in range(int(vals[0]), int(vals[1])+1):
            valid[x] = True
        for x in range(int(vals[3]), int(vals[4])+1):
            valid[x] = True

    for line in file:
        if line.startswith('nearby'):
            break

    for line in file:
        vals = [int(x) for x in line.split(',')]
        for x in vals:
            if not valid[x]:
                sum += x

print('Part 1:', sum)


class Field:
    def __init__(self, name, range1, range2):
        self.name = name
        self.range1 = range1
        self.range2 = range2
        self.fieldnum = []

fields = []

def removefield(f, i):
    if i not in f.fieldnum:
        return
    f.fieldnum.remove(i)
    if len(f.fieldnum) == 1:    # if there is only one option for this field, remove the option from all other fields.
        for f2 in fields:
            if f.name == f2.name:
                continue
            removefield(f2, f.fieldnum[0])

with open('day16.txt') as file:
    for line in file:
        if line == '\n':
            break

        line = line.split(':')
        vals = line[1].strip().replace('-',' ').split(' ')
        fields.append(Field(line[0], [int(vals[0]), int(vals[1])], [int(vals[3]), int(vals[4])]))

    for line in file:
        if line.startswith('your ticket'):
            break
    for line in file:
        myticket = [int(x) for x in line.split(',')]
        break
    for line in file:
        if line.startswith('nearby'):
            break

    n = len(fields)
    for f in fields:
        f.fieldnum = [x for x in range(n)]

    for line in file:
        vals = [int(x) for x in line.split(',')]
        validset = True
        for x in vals:
            validset = validset and valid[x]
        if not validset:
            continue

        for i,x in enumerate(vals):
            for f in fields:
                if i not in f.fieldnum:
                    continue
                if (x >= f.range1[0] and x <= f.range1[1]) or (x >= f.range2[0] and x <= f.range2[1]):
                    continue
                removefield(f, i)

p = 1
for f in fields:
    if f.name.startswith('departure'):
        p *= myticket[f.fieldnum[0]]
print('Part 2:', p)




