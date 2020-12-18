data = []

with open('in.txt') as f:
    for line in f:
        st = line.strip()
        data.append((st[0], int(st[1:])))

dir_map = {'N':{1, 0}, 'E': {0, 1}, 'S': {-1, 0}, 'W': {0, -1}}

def rot(dire, amount):
    assert amount % 90 == 0
    directions = ['N', 'E', 'S', 'W']
    times = amount // 90
    ind = directions.index(dire)
    return directions[(ind + times)%4]

def solve(li):
    vert = 0
    hori = 0
    dire = 'E'

    for action, val in li:
        if action == 'N':
            vert += val
        elif action == 'S':
            vert -= val
        elif action == 'E':
            hori += val
        elif action == 'W':
            hori -= val
        elif action == 'L':
            dire = rot(dire, -val)
        elif action == 'R':
            dire = rot(dire, val)
        elif action == 'F':
            v, h = dir_map[dire]
            vert += val * v
            hori += val * h

    return abs(vert)+abs(hori)

print(solve(data))