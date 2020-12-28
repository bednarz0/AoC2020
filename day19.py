class Rule:
    def __init__(self, id, rules):
        self.id = id
        self.rule = []
        self.msgset = set()

        args = rules.strip().strip('"').split(" ")
        if args[0] in 'ab':
            self.msgset.add(args[0])
            return
        subrule = []
        for a in args:
            if a == '|':
                self.rule.append(subrule)
                subrule = []
                continue
            subrule.append(a)
        self.rule.append(subrule)

rules = {}

def allchildrenset(allrules):
    for r in allrules:
        for s in r:
            if len(rules[s].msgset) == 0:
                return False
    return True

def validPart2(codeword, i1, i2):
    i = 0
    for _ in range(i1):
        if codeword[i:i+8] not in rules['8'].msgset:
            return False
        i += 8
    for _ in range(i2):
        if codeword[i:i + 8] not in rules['42'].msgset:
            return False
        i += 8
    for _ in range(i2):
        if codeword[i:i + 8] not in rules['31'].msgset:
            return False
        i += 8
    return True

with open('day19.txt') as file:
    for f in file:
        if f == '\n':
            break
        args = f.rstrip().split(":")

        id = args[0]
        rules[id] = Rule(id, args[1])

    while True:
        change = False

        for id, r in rules.items():
            if len(r.msgset) > 0:
                continue
            if allchildrenset(r.rule):
                change = True

                for s in r.rule:
                    if len(s) == 1:
                        for x in rules[s[0]].msgset:
                            r.msgset.add(x)
                    elif len(s) == 2:
                        for x in rules[s[0]].msgset:
                            for y in rules[s[1]].msgset:
                                r.msgset.add(x+y)

        if not change:
            break

    allowed = rules['0'].msgset

    cnt1, cnt2 = 0, 0
    for f in file:
        f = f.strip()
        if f in allowed:
            cnt1 += 1
        else:
            k = len(f)  # Part2 must match 8...  42... 31... where the number of 42's and 31's are equal.
            if k % 8:
                continue
            k = k // 8
            i1 = 2 - (k % 2)
            while i1 < k:
                i2 = (k - i1) // 2
                if validPart2(f, i1, i2):
                    cnt2 += 1
                    break
                i1 += 2

print('Part 1:', cnt1)
print('Part 2:', cnt1 + cnt2)
