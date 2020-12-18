data = []

with open('in.txt') as f:
    tmp = []
    for line in f:
        if not line.strip():
            data.append(tmp[:])
            tmp = []
            continue
        tmp.append([c for c in line.strip()])
    if tmp:
        data.append(tmp[:])

def solve(li):
    tot = 0
    for group in li:
        tot_set = set()
        for ans in group:
            tot_set.update(set(ans))
        tot += len(tot_set)

    return tot

print(solve(data))