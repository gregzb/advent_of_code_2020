from collections import deque

data= []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

def eval_expr(deque):
    tokens = []
    tmp_token = ''
    while deque:
        ch = deque.popleft()
        if ch == ' ':
            tokens.append(tmp_token)
            tmp_token = ''
        elif ch == '(':
            tmp_token = eval_expr(deque)
        elif ch == ')':
            break
        else:
            tmp_token += ch

    if tmp_token:
        tokens.append(tmp_token)

    while len(tokens) > 1:
        if '+' in tokens:
            idx = tokens.index('+')
            val = int(tokens[idx-1]) + int(tokens[idx+1])
            for i in range(idx+1, idx-2, -1):
                del tokens[i]
            tokens.insert(idx-1, val)
        else:
            curr = int(tokens[0])
            for i in range(1, len(tokens)-1, 2):
                curr *= int(tokens[i+1])
            return curr

    return int(tokens[0])

def solve(li):
    tot = 0
    for i, line in enumerate(li):
        tot += eval_expr(deque(line))
    return tot

print(solve(data))