Operator = {'+': lambda x,y:x+y,
            '*': lambda x,y:x*y}

def Evaluate1(s1):
    s2 = []    # remove all ()'s

    i = 0
    while i < len(s1):
        if s1[i] != '(':
            s2.append(s1[i])
            i += 1
            continue
        depth, j = 1, i+1
        while depth > 0:
            if s1[j] == '(':
                depth += 1
            elif s1[j] == ')':
                depth -= 1
            j += 1
        x = Evaluate1(s1[i+1:j-1])
        s2.append(str(x))
        i = j

    # Left to right evaluation

    z, i = int(s2[0]), 1
    while i < len(s2):
        z = Operator[s2[i]](z, int(s2[i+1]))
        i += 2
    return z

def Evaluate2(s1):
    s2 = []  # remove all ()

    i = 0
    while i < len(s1):
        if s1[i] != '(':
            s2.append(s1[i])
            i += 1
            continue
        depth, j = 1, i+1
        while depth > 0:
            if s1[j] == '(':
                depth += 1
            elif s1[j] == ')':
                depth -= 1
            j += 1
        s2.append(str(Evaluate2(s1[i+1:j-1])))
        i = j

    s3 = []  # process all + from left to right

    z, i = int(s2[0]), 1
    while i < len(s2):
        if s2[i] == '+':
            z = Operator['+'](z, int(s2[i+1]))
        else:
            s3.append(str(z))
            s3.append('*')
            z = int(s2[i+1])
        i += 2
    s3.append(str(z))

    # Last process *

    z, i = int(s3[0]), 1
    while i < len(s3):
        z = Operator['*'](z, int(s3[i+1]))
        i += 2

    return z

sum1, sum2 = 0, 0
with open('day18.txt') as f:
    for line in f:
        args = line.strip().replace('(', '( ').replace(')', ' )').split()
        sum1 += Evaluate1(args)
        sum2 += Evaluate2(args)
print('Part 1:', sum1)
print('Part 2:', sum2)