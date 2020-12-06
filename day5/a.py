data = []

with open('in.txt') as f:
    tmp_dict = {}
    for line in f:
        data.append(line.strip())

def get_val(thing):
    # each "thing" is really just two binary nums
    bot = thing[:7] # extract first 7 chars
    curr = 64 # 2^(7-1)
    val = 0 # the integer value we construct from the first part of string
    for ch in bot:
        if ch == 'B': # if B, add the current bit val, otherwise, its effectively a 0, so skip it
            val += curr
        curr //= 2 # next lower bit value

    top = thing[7:] # extract last 3 chars
    curr = 4 # 2^(3-1)
    val2 = 0 # the integer value we construct from the second part of string
    for ch in top:
        if ch == 'R':
            val2 += curr
        curr //= 2
    return val * 8 + val2

def solve(li):
    max_val = 0
    for thing in li:
        max_val = max(max_val, get_val(thing))
    return max_val

print(solve(data))