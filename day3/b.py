data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

def solve(li, dx, dy):
    sx = 0
    sy = 0

    cnt = 0

    while sy < len(data):
        if sy < len(data) and data[sy][sx % len(data[0])] == '#':
            cnt += 1
        sx += dx
        sy += dy
    return cnt

print(solve(data, 1, 1) * solve(data, 3, 1) * solve(data, 5, 1) * solve(data, 7, 1) * solve(data, 1, 2))