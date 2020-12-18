data = []

with open('in.txt') as f:
    for line in f:
        st = line.strip()
        data.append(st)

def solve(li):
    start_time = int(data[0])
    busses = data[1].split(',')
    busses = [int(x) for x in busses if x != 'x']

    min_time = start_time+1
    min_bus = -1
    for bus in busses:
        wait_time = bus - (start_time % bus)
        if wait_time < min_time:
            min_time = wait_time
            min_bus = bus

    return min_bus * min_time

print(solve(data))