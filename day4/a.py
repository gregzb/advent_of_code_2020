all_dicts = []

with open('in.txt') as f:
    tmp_dict = {}
    for line in f:
        entries = line.strip().split()
        for e in entries:
            a, b = e.split(':')
            tmp_dict[a]=b
        if not line.strip(): # this catches new lines and means that the current passport is done getting new entries, so add it to total list
            all_dicts.append(dict(tmp_dict))
            tmp_dict = {}
    if tmp_dict:
        all_dicts.append(dict(tmp_dict))

need = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def solve(dicts):
    cnt = 0
    for di in dicts:
        if len(set(di.keys()).intersection(need)) == 7: # check that all properties from need are present
            cnt += 1
    return cnt

print(solve(all_dicts))

print('\n'.split())