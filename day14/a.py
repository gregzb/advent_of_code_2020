data = []

with open('in.txt') as f:
    for line in f:
        st = line.strip().split(' = ')
        if st[0] != 'mask':
            st[1] = int(st[1])
            num_idxs = int(st[0].find('[') + 1), int(st[0].find(']'))
            st[0] = int(st[0][num_idxs[0]:num_idxs[1]])
        data.append(st)

def solve(li):
    curr_mask_mask = None
    curr_mask = None

    mem = {}

    for op, val in li:
        if op == 'mask':
            curr_mask_mask = int(val.replace('0', '1').replace('X', '0'), 2)
            curr_mask = int(val.replace('X', '0'), 2)
        else:
            mem[op] = (val & (~curr_mask_mask)) | curr_mask

    return sum(mem[key] for key in mem)

print(solve(data))