import itertools

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

    v = None

    mem = {}

    for op, val in li:
        if op == 'mask':
            curr_mask = [ch for ch in val]
        else:
            mem_val = bin(op)[2:].zfill(len(curr_mask))
            free_num = curr_mask.count('X')

            possibles = itertools.product(['o', 1], repeat=free_num)
            for possible in possibles:
                cnt = 0
                copy_mask = curr_mask[:]
                for i in range(len(copy_mask)):
                    if copy_mask[i] == 'X':
                        copy_mask[i] = str(possible[cnt])
                        cnt += 1

                curr = 0
                mult = 1
                for actual, mask in zip(mem_val[::-1], copy_mask[::-1]):
                    if mask == '0':
                        curr += int(actual) * mult
                    elif mask == 'o':
                        curr += 0 * mult
                    elif mask == '1':
                        curr += 1 * mult
                    else:
                        print("???")
                    mult <<= 1
                mem[curr] = val

    return sum(mem[key] for key in mem)

print(solve(data))