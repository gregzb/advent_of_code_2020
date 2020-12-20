rules = {}
messages = []

with open('in.txt') as f:
    for line in f:
        if not line.strip():
            break
        first_split = line.strip().split(": ")
        rule = int(first_split[0])
        if '"' in first_split[1]:
            rules[rule] = first_split[1].replace('"', '').strip()
        else:
            ors = first_split[1].strip().split(' | ')
            ints = [list(map(int, x.split(' '))) for x in ors]
            rules[rule] = ints

    for line in f:
        messages.append([ch for ch in line.strip()])


def dfs(rules, curr_node, target_str, idx):
    rule = rules[curr_node]
    if isinstance(rule, str):
        if idx < len(target_str) and target_str[idx] == rule:
            return idx + 1
        else:
            return -1
    else:
        for or_ in rule:
            curr_idx = idx
            for child_node in or_:
                new_idx = dfs(rules, child_node, target_str, curr_idx)
                curr_idx = new_idx
                if new_idx == -1:
                    break

            if curr_idx != -1:
                return curr_idx

        return -1

def matches(rules, message):
    return dfs(rules, 0, message, 0) == len(message)

def solve(rules, messages):
    return sum(matches(rules, message) for message in messages)

solved = solve(rules, messages)
print(solved)