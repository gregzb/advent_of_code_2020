data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

def solve(li):
    sx = 0
    sy = 0
    dx = 3
    dy = 1

    cnt = 0

    while sy < len(data):
        if sy < len(data) and data[sy][sx % len(data[0])] == '#':
            cnt += 1
        sx += dx
        sy += dy
    return cnt

print(solve(data))