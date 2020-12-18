data = []

with open('in.txt') as f:
    for line in f:
        st = line.strip()
        data.append((st[0], int(st[1:])))

def rot(w_vert, w_hori):
    return -w_hori, w_vert

def solve(li):
    vert = 0
    hori = 0
    w_vert = 1
    w_hori = 10
    dire = 'E'

    for action, val in li:
        if action == 'N':
            w_vert += val
        elif action == 'S':
            w_vert -= val
        elif action == 'E':
            w_hori += val
        elif action == 'W':
            w_hori -= val
        elif action == 'L':
            times = 4 + (-val // 90)
            for _ in range(times):
                w_vert, w_hori = rot(w_vert, w_hori)
        elif action == 'R':
            times = (val // 90) % 4
            for _ in range(times):
                w_vert, w_hori = rot(w_vert, w_hori)
        elif action == 'F':
            for _ in range(val):
                vert += w_vert
                hori += w_hori

    return abs(vert)+abs(hori)

print(solve(data))