passports = []

class Passport:
    def __init__(self, entries_):
        self.entries = entries_

    def has(self, need_set):
        return len(set(self.entries.keys()).intersection(need_set)) == len(need_set)

with open('in.txt') as f:
    tmp_dict = {}
    for line in f:
        entries = line.strip().split()
        for e in entries:
            a, b = e.split(':')
            tmp_dict[a]=b
        if not line.strip(): # this catches new lines and means that the current passport is done getting new entries, so add it to total list
            passports.append(Passport(dict(tmp_dict)))
            tmp_dict = {}
    if tmp_dict:
        passports.append(Passport(dict(tmp_dict)))

need = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def solve(passports):
    cnt = 0
    for passport in passports:
        if passport.has(need):
            cnt += 1
    return cnt

print(solve(passports))