class Instr:
    def __init__(self, op, arg):
        self.op = op
        self.arg = int(arg)
        self.cnt = 0

def CompileCode(filename):
    code = []
    with open('day08.txt') as f:
        for line in f:
            args = line.rstrip().split(sep=' ')
            code.append(Instr(args[0], args[1]))
    return code

class HGM:
    def __init__(self):
        self.code = []
        self.pc = 0
        self.acc = 0

    def load(self, code):
        self.code = code[:]

    def reset(self):
        self.pc = 0
        self.acc = 0
        for p in self.code:
            p.cnt = 0

    def run(self, loopdetect=False):
        while True:
            if self.pc < 0 or self.pc >= len(code):
                return 'exit', self.acc

            p = self.code[self.pc]
            if loopdetect == True and p.cnt > 0:
                return 'infloop', self.acc

            p.cnt += 1
            if p.op == 'nop':
                self.pc += 1
                continue
            if p.op == 'acc':
                self.acc += p.arg
                self.pc += 1
                continue
            if p.op == 'jmp':
                self.pc += p.arg
                continue


code = CompileCode('day08.txt')
gb = HGM()
gb.load(code)
gb.reset()
term, acc = gb.run(loopdetect=True)
print('Part 1:', acc)

swap = {'nop':'jmp', 'jmp':'nop'}

for p in code:
    if p.op == 'acc':
        continue
    p.op = swap[p.op]

    gb.load(code)
    gb.reset()
    term, acc = gb.run(loopdetect=True)
    if term == 'exit':
        print('Part 2:', acc)
        break
    p.op = swap[p.op]