from collections import *
import math
import bisect

data = None

with open('in.txt') as f:
    data = int(f.read().strip())

def sim(cups):
    new_deque = deque(cups)
    three = list(new_deque)[1:4]
    for _ in range(3):
        del new_deque[1]
    destination = cups[0]-1
    if destination == 0:
        destination = 9
    while destination in three or destination == 0:
        destination -= 1
        if destination == 0:
            destination = 9

    idx = new_deque.index(destination)
    for val in three[::-1]:
        new_deque.insert(idx+1, val)
    new_deque.rotate(-1)
    return new_deque
    

def solve(num):
    cups = deque([int(cup) for cup in str(num)])

    for _ in range(100):
        cups = sim(cups)

    idx = cups.index(1)

    cups.rotate(-idx)

    return ''.join([str(cup) for cup in list(cups)[1:]])

solved = solve(data)
print(solved)