data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

def get_val(st):
    return int(st.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)

def solve(li):
    all_ids = set(get_val(st) for st in li)

    # from previous part, we know max is 861
    # loop down from 861, first missing id is our seat
    for i in range(861, 0, -1):
        if i not in all_ids:
            return i
    return None

print(solve(data))