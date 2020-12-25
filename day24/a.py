from collections import *
import math
import bisect

data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip())

possible = ['e', 'se', 'sw', 'w', 'nw', 'ne']
offsets = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]

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

    

    return len([x for x in d.values() if x])

solved = solve(data)
print(solved)