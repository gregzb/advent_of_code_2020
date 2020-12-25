from collections import deque

players = None

with open('in.txt') as f:
    tmp = []
    players = f.read().split('\n\n')
    players = [play.split('\n')[1:] for play in players]
    players = [list(map(int, player)) for player in players]

results = {}

def get_winner(p0, p1):
    v0 = p0[0]
    v1 = p1[0]

    rem_0 = len(p0) - 1
    rem_1 = len(p1) - 1

    if v0 <= rem_0 and v1 <= rem_1:
        val = play_game(deque(list(p0)[1:1+v0]), deque(list(p1)[1:1+v1]))
        if val < 0:
            return (p1, p0)
        elif val > 0:
            return (p0, p1)
        else:
            print("???")
    elif v0 > v1:
        return (p0, p1)
    elif v1 > v0:
        return (p1, p0)
    else:
        print("???")

def hash_(p0, p1):
    return tuple(p0), tuple(p1)

max_v = 0

def play_game(p0, p1):
    global max_v
    seen = set()
    seen.add(hash_(p0, p1))

    while p0 and p1:
        winner, loser = get_winner(p0, p1)
        winner.append(winner.popleft())
        winner.append(loser.popleft())
        hashable = hash_(p0, p1)
        if hashable in seen:
            winner = p0
            break
        seen.add(hashable)

    is_winner = p0 == winner

    curr = 1
    score = 0
    while winner:
        val = winner.pop()
        score += curr*val
        curr += 1

    res = score if is_winner else -score

    max_v = max(max_v, len(seen))

    return res

def solve(p0, p1):
    return abs(play_game(p0, p1))

solved = solve(deque(players[0]), deque(players[1]))
print(solved)
# print(max_v)