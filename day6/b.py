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
        tot_set = {}
        for ans in group:
            for ch in ans:
                tot_set[ch] = tot_set.get(ch, 0) + 1

        tot += sum([tot_set[ch] == len(group) for ch in tot_set])

    return tot

print(solve(data))