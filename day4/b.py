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

            # annoying string validation
            byr_b = len(di['byr']) == 4 and 1920 <= int(di['byr']) <= 2002
            iyr_b = len(di['iyr']) == 4 and 2010 <= int(di['iyr']) <= 2020
            eyr_b = len(di['eyr']) == 4 and 2020 <= int(di['eyr']) <= 2030
            hgt_type = di['hgt'][-2:]
            hgt_b = False
            if hgt_type == 'cm':
                hgt_b = 150 <= int(di['hgt'][:-2]) <= 193
            elif hgt_type == 'in':
                hgt_b = 59 <= int(di['hgt'][:-2]) <= 76
            hcl_b = di['hcl'][0] == '#' and di['hcl'][1:].isalnum() # this should really reject every alphabetic char after f
            ecl_b = di['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            pid_b = di['pid'].isnumeric() and len(di['pid'])==9
            if byr_b and iyr_b and eyr_b and hgt_b and hcl_b and ecl_b and pid_b:
                cnt += 1
    return cnt

print(solve(all_dicts))