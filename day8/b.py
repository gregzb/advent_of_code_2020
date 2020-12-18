data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip().split())
        data[-1][-1] = int(data[-1][-1])

def try_list(li):
    acc = 0
    instr = 0

    visited = set()

    while True:
        if instr in visited:
            return None
        if instr >= len(li):
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

def solve(li):
    for i, item in enumerate(li):

        if item[0] == 'acc': continue

        if item[0] == 'nop':
            item[0] = 'jmp'
        elif item[0] == 'jmp':
            item[0] = 'nop'
        val = try_list(li)
        if val:
            return val
        if item[0] == 'nop':
            item[0] = 'jmp'
        elif item[0] == 'jmp':
            item[0] = 'nop'
    return None

print(solve(data))