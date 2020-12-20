from collections import defaultdict

data = {}

with open('in.txt') as f:
    tiles = f.read().split('\n\n')
    for tile in tiles:
        split_tile = tile.split('\n')
        num = int(split_tile[0][5:9])
        tile_vals = split_tile[1:]
        tile_vals = [[True if ch == '#' else False for ch in line] for line in tile_vals if line]
        data[num] = tile_vals

def rotate_tile(tile):
    new_tile = [[-1 for _ in tile] for __ in tile[0]]

    for i in range(len(tile)):
        for j in range(len(tile[0])):
            new_tile[j][len(tile)-i-1] = tile[i][j]
    return new_tile

def get_col(matrix, col):
    return [line[col] for line in matrix]

def solve(da):
    matches = defaultdict(int)
    for tile_key1 in da:
        tile1 = da[tile_key1]
        for tile_key2 in da:
            tile2 = da[tile_key2]
            if tile_key1 <= tile_key2:
                continue

            match = True
            tile_curr = tile2
            for i in range(4):
                if tile1[0] == tile_curr[0] or tile1[0] == tile_curr[0][::-1]:
                    match = True
                elif tile1[-1] == tile_curr[0] or tile1[-1] == tile_curr[0][::-1]:
                    match = True
                elif get_col(tile1, 0) == tile_curr[0] or get_col(tile1, 0) == tile_curr[0][::-1]:
                    match = True
                elif get_col(tile1, -1) == tile_curr[0] or get_col(tile1, -1) == tile_curr[0][::-1]:
                    match = True
                else:
                    match = False
                if match:
                    break
                tile_curr = rotate_tile(tile_curr)

            if match:
                matches[tile_key1] += 1
                matches[tile_key2] += 1

    # print(matches)
    corners = [val for val in matches if matches[val] == 2]
    i = 1
    for corner in corners:
        i *= corner
    return i

solved = solve(data)
print(solved)