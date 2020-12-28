cnt = 0
cnt2 = 0

with open('day02.txt') as f:
    for line in f:
        args = line.strip().split(' ')

        x = args[0].split('-')
        low = int(x[0])
        high = int(x[1])

        letter = args[1][0]
        passwd = args[2]

        lettercnt = passwd.count(letter)
        if lettercnt >= low and lettercnt <= high:
            cnt += 1

        x = 0
        if letter == passwd[low-1]:
            x += 1
        if letter == passwd[high-1]:
            x += 1
        if x == 1:
            cnt2 += 1

print('Part 1:', cnt)
print('Part 2:', cnt2)