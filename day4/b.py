passports = []

class Passport:
    def __init__(self, entries_):
        self.entries = entries_

    def has(self, need_set):
        return len(set(self.entries.keys()).intersection(need_set)) == len(need_set)

    def validate_byr(self):
        return len(self.entries['byr']) == 4 and 1920 <= int(self.entries['byr']) <= 2002

    def validate_iyr(self):
        return len(self.entries['iyr']) == 4 and 2010 <= int(self.entries['iyr']) <= 2020

    def validate_eyr(self):
        return len(self.entries['eyr']) == 4 and 2020 <= int(self.entries['eyr']) <= 2030

    def validate_hgt(self):
        hgt_type = self.entries['hgt'][-2:]
        hgt_b = False
        if hgt_type == 'cm':
            hgt_b = 150 <= int(self.entries['hgt'][:-2]) <= 193
        elif hgt_type == 'in':
            hgt_b = 59 <= int(self.entries['hgt'][:-2]) <= 76
        return hgt_b

    def validate_hcl(self):
        return self.entries['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in self.entries['hcl'][1:])

    def validate_ecl(self):
        return self.entries['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def validate_pid(self):
        return self.entries['pid'].isdigit() and len(self.entries['pid'])==9

    def validate_cid(self):
        return True

    def validate(self):
        return self.validate_byr() and self.validate_iyr() and self.validate_eyr() and self.validate_hgt() and self.validate_hcl() and self.validate_ecl() and self.validate_pid() and self.validate_cid()

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
            if passport.validate():
                cnt += 1
    return cnt

print(solve(passports))