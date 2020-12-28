class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = []
        self.containsshinygold = False

bags = {}
with open('day07.txt') as f:
    for line in f:
        args = line.rstrip().split(' ')
        bagname = args[0]+' '+args[1]
        p = Bag(bagname)
        i = 4
        while i < len(args):
            if args[i] != 'no':
                p.contains.append((int(args[i]), args[i+1]+' '+args[i+2]))
            i += 4
        bags[bagname] = p

p = []
p.append('shiny gold')
cnt = 0
while len(p) > 0:
    q = p.pop(0)
    for bagname, bag in bags.items():
        if bag.containsshinygold:
            continue
        for c in bag.contains:
            if q == c[1]:
                bag.containsshinygold = True
                cnt += 1
                p.append(bagname)
                break
print('Part 1:', cnt)

def cntbagsinside(name):
    p = bags[name]
    cnt = 0
    for q in p.contains:
        cnt += q[0] * (1 + cntbagsinside(q[1]))
    return cnt
print('Part 2:', cntbagsinside('shiny gold'))




