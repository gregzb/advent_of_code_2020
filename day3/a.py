data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip().split())

def solve(li):
    return 0

print(solve(data))