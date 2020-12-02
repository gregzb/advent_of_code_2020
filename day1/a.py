l = []
with open('in.txt') as f:
    for line in f:
        l.append(int(line.strip()))

# check if any pair adds up to 2020, if so, return their product
# O(n) is better, but takes slightly longer to code
def solve(l):
    for a in l:
        for b in l:
            if a+b == 2020:
                return a*b

print(solve(l))