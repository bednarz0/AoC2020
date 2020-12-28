def loadDecks():
    p1deck, p2deck = [], []
    p = p1deck
    with open('day22.txt') as file:
        for f in file:
            if f.startswith('Player'):
                continue
            if f == '\n':
                p = p2deck
                continue
            p.append(int(f))
    return p1deck, p2deck

def playPart1(p1deck, p2deck):
    while True:
        if len(p1deck) == 0:
            winner = 'P2'
            p = p2deck
            break
        elif len(p2deck) == 0:
            winner = 'P1'
            p = p1deck
            break

        p1, p2 = p1deck.pop(0), p2deck.pop(0)
        if p1 > p2:
            p1deck.append(p1)
            p1deck.append(p2)
        else:
            p2deck.append(p2)
            p2deck.append(p1)
    return winner, sum([(i+1)*n for i,n in enumerate(p[::-1])])

p1deck, p2deck = loadDecks()
winner, score = playPart1(p1deck, p2deck)
print('Part 1:', score, winner, 'wins')

def playPart2(p1deck, p2deck):
    history = set()
    while True:
        if len(p1deck) == 0:
            winner, p = 'P2', p2deck
            break
        elif len(p2deck) == 0:
            winner, p = 'P1', p1deck
            break

        if (tuple(p1deck), tuple(p2deck)) in history:
            winner, p = 'P1', p1deck
            break
        history.add((tuple(p1deck), tuple(p2deck)))

        p1, p2 = p1deck.pop(0), p2deck.pop(0)
        if p1 <= len(p1deck) and p2 <= len(p2deck):
            winner, _ = playPart2(p1deck[:p1], p2deck[:p2])
        elif p1 > p2:
            winner = 'P1'
        else:
            winner = 'P2'

        if winner == 'P1':
            p1deck += [p1, p2]
        else:
            p2deck += [p2, p1]
    return winner, sum([(i+1)*n for i,n in enumerate(p[::-1])])

p1deck, p2deck = loadDecks()
winner, score = playPart2(p1deck, p2deck)
print('Part 2:', score, winner, 'wins')

