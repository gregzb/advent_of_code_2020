data = []

with open('in.txt') as f:
    for line in f:
        data.append(int(line.strip()))

def solve(li):
    sorted_l = sorted(li)
    sorted_l.append(sorted_l[-1]+3)
    n = len(sorted_l)
    dp = [0 for _ in range(sorted_l[-1] + 1)]
    dp[0] = 1
    for val in sorted_l:
        tmp = 0
        for i in range(max(0, val-3), val):
            dp[val] += dp[i]

    return dp[-1]

print(solve(data))