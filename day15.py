numbers = [0,20,7,16,1,18,15]

while len(numbers) < 2020:
    j = len(numbers) - 2
    while True:
        if j < 0:
            numbers.append(0)
            break
        if numbers[j] == numbers[len(numbers)-1]:
            numbers.append(len(numbers) - 1 - j)
            break
        j -= 1
print('Part 1:', numbers[2019])

numbers = [0,20,7,16,1,18,15]

mem = {}
N = 30000000
pos = 1
for x in numbers[:len(numbers)-1]:
    mem[x] = pos
    pos += 1
last = numbers[-1]

while pos < N:
    if last in mem:
        new = pos - mem[last]
    else:
        new = 0

    mem[last] = pos
    last = new
    pos += 1

print('Part 2:', last)

