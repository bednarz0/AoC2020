with open('day25.txt') as f:
    cardPK = int(f.readline())
    doorPK = int(f.readline())

x = 1
cardLoopSize = 0

while x != cardPK:
    x = (x * 7) % 20201227
    cardLoopSize += 1

ec = 1
for _ in range(cardLoopSize):
    ec = (ec * doorPK) % 20201227

print('Part 1:', ec)
