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

# clockwise rotation
def rotate_tile(tile):
    new_tile = [[-1 for _ in tile] for __ in tile[0]]

    for i in range(len(tile)):
        for j in range(len(tile[0])):
            new_tile[j][len(tile)-i-1] = tile[i][j]
    return new_tile

def flip_tile(tile):
    new_tile = [[-1 for _ in tile[0]] for __ in tile]

    for i in range(len(tile)):
        for j in range(len(tile[0])):
            new_tile[i][len(tile)-j-1] = tile[i][j]
    return new_tile

def get_col(matrix, col):
    return [line[col] for line in matrix]

image = {}
seen = set()
def dfs(tile_dict, tile_id, x, y):
    if tile_id in seen:
        return
    seen.add(tile_id)

    image[(x,y)] = tile_dict[tile_id]

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    vals = [tile_dict[tile_id][0], get_col(tile_dict[tile_id], 0), tile_dict[tile_id][-1], get_col(tile_dict[tile_id], -1)]
    get_vals = [lambda tile: tile[0], lambda tile: get_col(tile, 0), lambda tile: tile[-1], lambda tile: get_col(tile, -1)]

    for di in range(4):
        ox, oy = dirs[di]
        n_x = x+ox
        n_y = y+oy
        if (n_x, n_y) in image:
            continue

        for other_id in list(tile_dict.keys()):
            if other_id == tile_id:
                continue

            opposite = (di + 2) % 4

            other_tile = tile_dict[other_id]
            flipped = flip_tile(other_tile)

            found = True

            for _ in range(4):
                if vals[di] == get_vals[opposite](other_tile):
                    tile_dict[other_id] = other_tile
                    dfs(tile_dict, other_id, n_x, n_y)
                elif vals[di] == get_vals[opposite](flipped):
                    tile_dict[other_id] = flipped
                    dfs(tile_dict, other_id, n_x, n_y)
                else:
                    found = False
                if found:
                    break
                other_tile = rotate_tile(other_tile)
                flipped = rotate_tile(flipped)

            if found:
                break

def print_tile(tile):
    for line in tile:
        print(''.join(['#' if ch else '.' for ch in line]))

def shrink_tile(tile):
    chopped_rows = tile[1:-1]
    chopped_cols = [line[1:-1] for line in chopped_rows]
    return chopped_cols

def count_true(tile):
    return sum(sum([ch for ch in line]) for line in tile)

def find_dragons(tile):
    dragon = [  '                  # ',
                '#    ##    ##    ###',
                ' #  #  #  #  #  #   ']

    dragon = [[True if ch == '#' else False for ch in line] for line in dragon]

    dragon_rows = len(dragon)
    dragon_cols = len(dragon[0])

    cnt = 0

    for row in range(len(tile)-(dragon_rows-1)):
        for col in range(len(tile[0]) - (dragon_cols-1)):
            is_dragon = True
            for dr in range(dragon_rows):
                for dc in range(dragon_cols):
                    if dragon[dr][dc] == True and tile[row+dr][col+dc] == False:
                        is_dragon = False

            if is_dragon:
                cnt += 1
    return 0 if cnt == 0 else count_true(tile) - (count_true(dragon) * cnt)

def solve(da):
    root_tile = 1213 # found from part a, its a corner tile
    dfs(da, root_tile, 0, 0)

    for loc in image:
        image[loc] = shrink_tile(image[loc])

    max_val, min_val = list(image.keys())[0][0], list(image.keys())[0][0]
    for ke in image:
        min_val = min(min_val, ke[0])
        max_val = max(max_val, ke[0])

    im_square = max_val-min_val+1

    unit = len(image[(0,0)])

    final_image = [[-1 for _ in range(12*unit)] for __ in range(im_square*unit)]
    for r in range(im_square):
        for c in range(im_square):
            t_r = im_square-1-r
            for tr in range(unit):
                for tc in range(unit):
                    final_image[t_r*unit+tr][c*unit+tc] = image[(c, r)][tr][tc]

    flipped = flip_tile(final_image)
    for i in range(4):
        a = find_dragons(final_image)
        b = find_dragons(flipped)
        if a: return a
        if b: return b
        final_image = rotate_tile(final_image)
        flipped = rotate_tile(flipped)


solved = solve(data)
print(solved)