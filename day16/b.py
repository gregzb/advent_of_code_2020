ranges = {}
ticket = []
other_tickets = []

with open('in.txt') as f:
    for line in f:
        if not line.strip():
            break
        range_line = line.strip().split(': ')
        field = range_line[0]
        actual_values = list(map(lambda x: list(map(int, x.split('-'))), range_line[1].split(' or ')))
        ranges[field] = actual_values
    
    f.readline()
    ticket = list(map(int, f.readline().strip().split(',')))
    f.readline()
    f.readline()
    for line in f:
        other_tickets.append(list(map(int, line.strip().split(','))))

def validate_field(ranges, field, value):
    field_range = ranges[field]
    return field_range[0][0] <= value <= field_range[0][1] or field_range[1][0] <= value <= field_range[1][1]

value_to_field = [set() for _ in range(1000)]

for val in range(1000):
    for ran in ranges:
        if validate_field(ranges, ran, val):
            value_to_field[val].add(ran)

# print(value_to_field)

def solve(ranges, ticket, other_tickets):
    valid_tickets = []
    for ti in other_tickets:
        if not [val for val in ti if not any([validate_field(ranges, ran, val) for ran in ranges])]:
            valid_tickets.append(ti)

    used = dict()
    cols = len(valid_tickets[0])
    for i in range(cols):
        for col in range(cols):
            curr_set = set([ran for ran in ranges])
            curr_set.difference_update(used.keys())
            for ti in valid_tickets:
                curr_set.intersection_update(value_to_field[ti[col]])
            if len(curr_set) == 1:
                used[list(curr_set)[0]] = col
                break

    tot = 1
    for field in used:
        if 'departure' in field:
            idx = used[field]
            tot *= ticket[idx]

    return tot

print(solve(ranges, ticket, other_tickets))