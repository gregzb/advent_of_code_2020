data = []

with open('in.txt') as f:
    for line in f:
        data=list(map(int, line.strip().split(',')))

def solve(li):
    seen = {}
    for i in range(len(data)):
        seen[data[i]] = i

    next_val = 0

    for i in range(len(data), 2020):
        curr_val = next_val
        next_val = i - seen.get(curr_val, i)
        seen[curr_val] = i
    return curr_val

print(solve(data))