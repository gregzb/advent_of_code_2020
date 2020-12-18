data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip().split())
        data[-1][-1] = int(data[-1][-1])

print(data)

def solve(li):
    acc = 0
    instr = 0

    visited = set()

    while True:
        if instr in visited:
            return acc
        visited.add(instr)
        op_name, op_val = li[instr]
        if op_name == 'acc':
            acc += op_val
        elif op_name == 'jmp':
            instr += op_val-1
        elif op_name == 'nop':
            pass
        else:
            print('??')
        instr += 1

    return None

print(solve(data))