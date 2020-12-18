from collections import deque

data = []

with open('in.txt') as f:
    for line in f:
        data.append(int(line.strip()))

def is_valid(next_val, twen):
    for i in range(len(twen)-1):
        for j in range(i+1, len(twen)):
            if twen[i] + twen[j] == next_val:
                return True

def solve(li):
    twen = deque(li[:25])

    next_idx = 25
    while is_valid(li[next_idx], twen):
        twen.popleft()
        twen.append(li[next_idx])
        next_idx += 1

    return li[next_idx]

print(solve(data))