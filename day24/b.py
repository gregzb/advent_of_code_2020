from collections import *
import math
import bisect

data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

possible = ['e', 'se', 'sw', 'w', 'nw', 'ne']
offsets = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]

def fill_dict(d):
    ix = min([x for x,y in d if d[(x,y)]])
    iy = min([y for x,y in d if d[(x,y)]])
    ax = max([x for x,y in d if d[(x,y)]])
    ay = max([y for x,y in d if d[(x,y)]])

    for x in range(ix-1, ax+2):
        for y in range(ix-1, ax+2):
            val = d[(x,y)]
            d[(x,y)] = val

def sim(d):
    copy = defaultdict(lambda: False, d)

    for x,y in list(d.keys()):
        cnt = 0
        for ox,oy in offsets:
            if d[(x+ox,y+oy)]:
                cnt += 1
        
        if d[(x,y)]:
            if cnt == 0 or cnt > 2:
                copy[(x,y)] = False
        else:
            if cnt == 2:
                copy[(x,y)] = True

    fill_dict(copy)

    return copy


def solve(li):
    all_converted = []
    for line in li:
        converted = []
        i = 0
        while i < len(line):
            for idx, p in enumerate(possible):
                if line[i:i+len(p)] == p:
                    converted.append(idx)
                    i += len(p)
                    break
        all_converted.append(converted)

    d = defaultdict(lambda: False)

    for converted in all_converted:
        x, y = 0, 0
        for off_idx in converted:
            ox, oy = offsets[off_idx]
            x += ox
            y += oy
        d[(x, y)] = not d[(x,y)]

    fill_dict(d)

    for _ in range(100):
        print(_)
        d = sim(d)

    return len([x for x in d.values() if x])

solved = solve(data)
print(solved)