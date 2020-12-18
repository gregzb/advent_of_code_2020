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

def solve(ranges, ticket, other_tickets):
    tot = 0
    valid_tickets = []
    for ti in other_tickets:
        tot += sum([val for val in ti if not any([validate_field(ranges, ran, val) for ran in ranges])])
    return tot

print(solve(ranges, ticket, other_tickets))