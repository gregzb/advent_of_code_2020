from collections import deque

players = None

with open('in.txt') as f:
    tmp = []
    players = f.read().split('\n\n')
    players = [play.split('\n')[1:] for play in players]
    players = [list(map(int, player)) for player in players]
        
def solve(players):
    p0, p1 = players
    p0 = deque(p0)
    p1 = deque(p1)

    while p0 and p1:
        print(len(p0), len(p1))
        a, b = p0.popleft(), p1.popleft()
        if a > b:
            p0.append(a)
            p0.append(b)
        elif a < b:
            p1.append(b)
            p1.append(a)
        else:
            print('???')

    winner = p0 if p0 else p1

    curr = 1
    score = 0
    while winner:
        val = winner.pop()
        score += curr*val
        curr += 1

    return score

solved = solve(players)
print(solved)