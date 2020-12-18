import math
data = []

# CHINESE REMAINDER THEOREM

with open('in.txt') as f:
    for line in f:
        st = line.strip()
        data.append(st)

# https://takp.me/posts/compute-the-modular-inverse-using-extended-gcd/
# Python's xgcd function. 
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def solve(li):
    busses = data[1].split(',')
    busses = [(i, int(x)) for i, x in enumerate(busses) if x != 'x']

    nums = [x[1] for x in busses]
    rems = [x[1] - x[0] for x in busses]

    M = 1
    for num in nums:
        M *= num

    tot = 0
    for i in range(len(nums)):
        ai = rems[i]
        bi = M // nums[i]
        gcd_, a, b = xgcd(bi, nums[i])
        tot += ai*bi*a
    tot %= M
    return tot


print(solve(data))