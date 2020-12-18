data = []

with open('in.txt') as f:
    for line in f:
        data.append(int(line.strip()))

def solve(li):
    sorted_l = sorted(li)
    sorted_l.append(sorted_l[-1]+3)
    prev = 0
    d = {0: 0, 1:0, 2:0, 3:0}
    for val in sorted_l:
        d[val-prev] += 1
        prev = val
    return d[1] * d[3]

print(solve(data))