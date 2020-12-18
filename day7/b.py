data = []

with open('in.txt') as f:
    for line in f:
        data.append(line.strip().split(" contain "))
        data[-1][0] = data[-1][0][:-5]
        data[-1][1] = data[-1][1].split(', ')
        if data[-1][1][0] == 'no other bags.':
            data[-1][1] = []

        for i, entry in enumerate(data[-1][1]):
            data[-1][1][i] = data[-1][1][i].replace('.', '').replace(' bags', '').replace(' bag', '')
            num = int(data[-1][1][i].split()[0])
            remaining = ' '.join(data[-1][1][i].split()[1:])
            data[-1][1][i] = (num, remaining)

def dfs(graph, curr):
    if curr not in graph or len(graph[curr]) == 0:
        return 1
    cnt = 0
    for child_num, child_name in graph[curr]:
        cnt += child_num * dfs(graph, child_name)
    return cnt + 1

def solve(li):
    children = {}
    for line in li:
        children[line[0]] = line[1]
    return dfs(children, 'shiny gold') - 1

print(solve(data))