allergens = {}
iCnt = {}

with open('day21.txt') as file:
    for f in file:
        args = f.strip().replace(',', ' ').replace(')', ' ').split()

        i = args.index('(contains')
        ingredients = args[:i]
        allergies = args[i+1:]

        for i in ingredients:
            if i not in iCnt:
                iCnt[i] = 0
            iCnt[i] += 1

        for a in allergies:
            if a not in allergens:
                allergens[a] = set(ingredients)
            else:
                allergens[a] = allergens[a] & set(ingredients)

    q = []
    for a,s in allergens.items():
        if len(s) == 1:
            q.append((a, list(s)[0]))

    while len(q) > 0:
        adel, idel = q.pop(0)

        for a,s in allergens.items():
            if a == adel:
                continue

            if idel in s:
                s.remove(idel)
                if len(s) == 1:
                    q.append((a, list(s)[0]))

allallergens = set()
dangerlist = []
for a,s in allergens.items():
    allallergens |= s
    dangerlist.append((a, list(s)[0]))

sum = 0
for i, cnt in iCnt.items():
    if i not in allallergens:
        sum += cnt

print('Part 1:', sum)

dangerlist.sort(key=lambda x:x[0])

print('Part 2:', ''.join([x[1]+',' for x in dangerlist]).rstrip(','))



