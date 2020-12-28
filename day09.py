with open('day09.txt') as f:
    series = [int(x) for x in f]

def isvalidcode(x, s):
    for i in range(24):
        for j in range(i+1,25):
            if x == s[i]+s[j]:
                return True
    return False

i = 25
while isvalidcode(series[i], series[i-25:i]):
    i += 1

badcode = series[i]
print('Part 1:', badcode)

head, tail, sum = 0, 0, 0
while sum != badcode:
    if sum < badcode:
        sum += series[tail]
        tail += 1
    else:
        sum -= series[head]
        head += 1

print('Part 2:', max(series[head:tail]) + min(series[head:tail]))

