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
            return [idx + 1]
        else:
            return [-1]
    else:
        idxes = []
        for or_ in rule:
            curr_idxes = [idx]
            next_idxes = []
            for child_node in or_:
                for curr_idx in curr_idxes:
                    new_idxes = dfs(rules, child_node, target_str, curr_idx)
                    new_idxes = [idx for idx in new_idxes if idx != -1]
                    next_idxes.extend(new_idxes)

                curr_idxes = next_idxes
                next_idxes = []

            idxes.extend(curr_idxes)

        return idxes

def matches(rules, message):
    return sum(idx == len(message) for idx in dfs(rules, 0, message, 0))

def solve(rules, messages):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return sum(matches(rules, message) for message in messages)

solved = solve(rules, messages)
print(solved)