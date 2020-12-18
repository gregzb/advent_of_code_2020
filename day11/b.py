data = []

with open('in.txt') as f:
    for line in f:
        data.append([ch for ch in line.strip()])

def copy(li):
    return [inner[:] for inner in li]

def valid(row, col, curr):
    return row >= 0 and row < len(curr) and col >= 0 and col < len(curr[0])

def sim(curr):
    tmp = copy(curr)
    for row in range(len(curr)):
        for col in range(len(curr[0])):
            state = curr[row][col]
            near_row = [1, -1, 1, -1, 0, 0, 1, -1]
            near_col = [1, 1, -1, -1, 1, -1, 0, 0]

            num_occ = 0
            for i in range(8):
                new_dir_r = near_row[i]
                new_dir_c = near_col[i]
                new_row = row + near_row[i]
                new_col = col + near_col[i]
                while valid(new_row, new_col, curr):
                    if curr[new_row][new_col] == '#':
                        num_occ += 1
                        break
                    if curr[new_row][new_col] == 'L':
                        break
                    new_row += new_dir_r
                    new_col += new_dir_c

            if state == '.': continue
            elif state == 'L':
                if num_occ == 0:
                    tmp[row][col] = '#'
            elif state == '#':
                if num_occ >= 5:
                    tmp[row][col] = 'L'
            else:
                print("???")
    return tmp

def count_occ(tmp):
    occ = 0

    for row in range(len(tmp)):
        for col in range(len(tmp[0])):
            state = tmp[row][col]
            if state == '#':
                occ += 1
    return occ

def solve(li):
    tmp = li
    for i in range(300):
        tmp = sim(tmp)

    return count_occ(tmp)

print(solve(data))