data = []

with open('in.txt') as f:
    for line in f:
        data.append(int(line.strip()))

def solve(li):
    target = 1212510616

    prefix = [0 for _ in range(len(li) + 1)]
    for i in range(1, len(li) + 1):
        prefix[i] = prefix[i-1] + li[i-1]

    for i in range(0, len(li)):
        for j in range(i+1, len(li)+1):
            if prefix[j] - prefix[i] == target:
                the_range = li[i:j]
                return min(the_range) + max(the_range)

print(solve(data))