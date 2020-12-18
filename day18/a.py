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

    curr = int(tokens[0])
    for i in range(1, len(tokens)-1, 2):
        op = tokens[i]
        num = int(tokens[i+1])
        if op == '+':
            curr += num
        elif op == '*':
            curr *= num
        else:
            print("???")

    return curr

def solve(li):
    tot = 0
    for line in li:
        tot += eval_expr(deque(line))
    return tot

print(solve(data))