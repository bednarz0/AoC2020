
class MyNum:
    def __init__(self, x):
        self.x = int(x)

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x * other.x

    def __rsub__(self, other):
        return self.x * other.x

    def get(self):
        return self.x

sum1, sum2 = 0, 0
with open('day18b.txt') as f:
    for line in f:
        args = line.strip().replace('*', '-').replace('(', '( ').replace(')', ' )').split()
        s = ''
        for i,x in enumerate(args):
            if x[0] in '0123456789':
                args[i] = 'MyNum('+x+')'
            s += args[i]

        print(s)
#        s = 'MyNum(2) + MyNum(5)'
        y = eval(s)
        print(y)


print('Part 1:', sum1)
print('Part 2:', sum2)