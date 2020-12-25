from collections import *
import math
import bisect

data = []

with open('in.txt') as f:
    for line in f:
        data.append(int(line.strip()))


def get_loop(subject_num, num):
    i = 0
    s = 1
    while s != num:
        s *= subject_num
        s %= 20201227
        i += 1
    return i

def loops(subject_num, loops):
    i = 0
    s = 1
    while i < loops:
        s *= subject_num
        s %= 20201227
        i += 1
    return s

def solve(li):
    loop_card, loop_door = get_loop(7, li[0]), get_loop(7, li[1])
    return loops(li[0], loop_door)

solved = solve(data)
print(solved)