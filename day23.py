from collections import deque

def move(q, n):
   p = []
   m = max(q)

   for _ in range(n):
        c = q[-1]
        for _ in range(3):
            p.append(q.popleft())
        while True:
            c -= 1
            if c == 0:
                c = m
            if c in p:
                continue
            break
        i = q.index(c)
        q.rotate(m-4-i)
        for _ in range(3):
            q.appendleft(p.pop())
        q.rotate(i)

start = '712643589'
#start = '389125467'

q = deque([int(x) for x in start])
q.rotate(-1)

move(q, 100)

i = q.index(1) + 1
labels = ''
for j in range(8):
    labels += str(q[(i+j)%9])
print('Part 1:', labels)

class Cup:
    def __init__(self, n):
        self.n = n
        self.next = None
        self.inCircle = True

    def insert3(self, q):
        p = self.next
        self.next = q
        q.inCircle = True
        q = q.next
        q.inCircle = True
        q = q.next
        q.inCircle = True
        q.next = p

    def remove3(self):
        p, q = self.next, self.next
        for _ in range(3):
            q.inCircle = False
            q = q.next
        self.next = q
        return p

N = 1000000
startorder = [int(x) for x in start]
startorder.extend([x for x in range(10, N+1)])

cups = [Cup(x) for x in range(N+1)]
for m,n in zip(startorder[:-1], startorder[1:]):
    cups[m].next = cups[n]
cups[startorder[-1]].next = cups[startorder[0]]

current = cups[int(start[0])]

for _ in range(10000000):
#    p = current
#    for _ in range(N):
#        print(p.n, sep=' ', end='')
#        p = p.next
#    print()

    pickup = current.remove3()
#    print('Pickup', pickup.n, pickup.next.n, pickup.next.next.n)

    destnum = current.n - 1
    while True:
        if destnum == 0:
            destnum = N
        if not cups[destnum].inCircle:
            destnum -= 1
            continue
        break
#    print('Dest', destnum)
    cups[destnum].insert3(pickup)
    current = current.next

print('Part 2:', cups[1].next.n * cups[1].next.next.n)

