takenSeats = []
with open('day05.txt') as f:
    for line in f:
        id = 0
        for c in line.rstrip():
            id *= 2
            if c in 'BR':
                id += 1
        takenSeats.append(id)
print('Part 1:', max(takenSeats))

takenSeats.sort()
i = 0
while takenSeats[i] + 1 == takenSeats[i+1]:
    i += 1
print('Part 2:', takenSeats[i]+1)


