from collections import Counter

data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip().split())
        data[-1][0] = list(map(int, data[-1][0].split('-'))) # separate range string into ints
        data[-1][1] = data[-1][1][:-1] # remove colon from char

def solve(li):
    cnt = 0
    for line in li:
        ra = line[0] # range
        ch = line[1] # character restriction
        st = line[2] # the string

        if (st[ra[0]-1] == ch or st[ra[1]-1] == ch) and not (st[ra[0]-1] == ch and st[ra[1]-1] == ch): # only one of the chars are allow to match ch, not both
            cnt += 1
    return cnt

print(solve(data))