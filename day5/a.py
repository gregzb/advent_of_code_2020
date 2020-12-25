data = []

with open('in.txt') as f:
    data = [line.strip() for line in f]

def get_val(st):
    return int(st.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)

def solve(li):
    return max(get_val(st) for st in li)

print(solve(data))