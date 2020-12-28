import re

cnt = 0
validset = set(['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:'])
passport = set()

with open('day04.txt') as f:
    for line in f:
        if line[0] == '\n':
            if passport & validset == validset:
                cnt += 1
            passport.clear()
        else:
            for args in line.strip().split(' '):
                passport.add(args[:4])
if passport == validset:
    cnt += 1
print('Part 1:', cnt)

cnt = 0
passport.clear()

validator = re.compile('(^byr:(19[2-9][0-9]|200[0-2])$'
                        '|^iyr:20(1[0-9]|20)$'
                        '|^eyr:20(2[0-9]|30)$'
                        '|^hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$'
                        '|^hcl:#[0-9a-f]{6,6}$'
                        '|^ecl:(amb|blu|brn|gry|grn|hzl|oth)$'
                        '|^pid:[0-9]{9,9}$)')

with open('day04.txt') as f:
    for line in f:
        if line[0] == '\n':
            if passport == validset:
                cnt += 1
            passport.clear()
        else:
            for args in line.rstrip().split(' '):
                if validator.match(args) != None:
                    passport.add(args[:4])
if passport == validset:
    cnt += 1
print('Part 2:', cnt)
