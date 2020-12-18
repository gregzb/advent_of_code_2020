from collections import defaultdict
import itertools

data= []

with open('in.txt') as f:
    for line in f:
        data.append([False if ch == '.' else True for ch in line.strip()])

class Cube:
    def __init__(self, cube):
        self.cube = defaultdict(lambda: False)
        for i in range(len(cube)):
            for j in range(len(cube[0])):
                self.cube[(j, i, 0, 0)] = cube[i][j]
        
        self.calc_min_max()

    def calc_min_max(self):
        self.maxes = [None, None, None, None]
        self.mins = [None, None, None, None]
        for entry in self.cube:
            if not self.cube[entry]:
                continue
            for i in range(4):
                if self.maxes[i] == None or entry[i]+1 > self.maxes[i]:
                    self.maxes[i] = entry[i]+1
                if self.mins[i] == None or entry[i]-1 < self.mins[i]:
                    self.mins[i] = entry[i]-1

    def count_neighboring(self, x, y, z, w):
        dirs = [-1, 0, 1]
        tot = 0
        for xo, yo, zo, wo in itertools.product(dirs, repeat=4):
            if xo==0 and yo==0 and zo==0 and wo == 0:
                continue
            tot += int(self.cube[(x+xo,y+yo,z+zo, w+wo)])
        return tot

    def count_active(self):
        return sum(int(self.cube[k]) for k in self.cube)

    def sim(self):
        copy = Cube([])
        copy.cube = defaultdict(lambda: False, {k: self.cube[k] for k in self.cube})

        for x in range(self.mins[0], self.maxes[0]+1):
            for y in range(self.mins[1], self.maxes[1]+1):
                for z in range(self.mins[2], self.maxes[2]+1):
                    for w in range(self.mins[3], self.maxes[3]+1):
                        neighbors = self.count_neighboring(x, y, z, w)
                        if self.cube[(x,y,z, w)]:
                            if not (neighbors == 2 or neighbors == 3):
                                copy.cube[(x,y,z,w)] = False
                        else:
                            if neighbors == 3:
                                copy.cube[(x,y,z,w)] = True
        
        copy.calc_min_max()

        return copy
                

def solve(li):
    cube = Cube(li)
    for i in range(6):
        new_cube = cube.sim()
        cube = new_cube
    return cube.count_active()

print(solve(data))