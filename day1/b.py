l = []
with open('in.txt') as f:
    for line in f:
        l.append(int(line.strip()))

# check if any triplet adds up to 2020, if so, return their product
# O(n^2) is better, but takes slightly longer to code
def solve(l):
    for a in l:
        for b in l:
            for c in l:
                if a+b+c == 2020:
                    return a*b*c

print(solve(l))