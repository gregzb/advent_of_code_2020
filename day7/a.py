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

print(data)

seen = set()
def dfs(graph, root):
    global seen
    if root not in seen:
        seen.add(root)
        cnt = 0
        if root in graph:
            for child in graph[root]:
                dfs(graph, child)
    return

def solve(li):
    global seen
    parents = {}
    for line in li:
        parent = line[0]
        children = line[1]
        for child_num, child_string in children:
            if child_string not in parents:
                parents[child_string] = []
            parents[child_string].append(parent)

    dfs(parents, 'shiny gold')
    return len(seen) - 1

print(solve(data))