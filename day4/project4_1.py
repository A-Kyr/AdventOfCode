def get_passports(filename):
    with(open(filename)) as f:
        lines = f.readlines()

    passports = []
    word = ''
    for line in lines:
        if line != '\n':
            line = line.strip('\n')
            word = word + line + ' '
        else:
            word = word.split(' ')
            word = word[:-1]
            passports.append(word)
            word = ''
    return passports


def is_valid(passport):
    count = 0
    for attribute in passport:
        attribute = attribute.split(':')
        type = attribute[0]
        value = attribute[1]
        if type != 'cid' and validate(type, value):
            count += 1

    return count >= 7


def validate(type, value):
    if type == 'byr':
        if not validate_byr(value):
            return False
    elif type == 'iyr':
        if not validate_iyr(value):
            return False
    elif type == 'eyr':
        if not validate_eyr(value):
            return False
    elif type == 'hgt':
        if not validate_hgt(value):
            return False
    elif type == 'hcl':
        if not validate_hcl(value):
            return False
    elif type == 'ecl':
        if not validate_ecl(value):
            return False
    elif type == 'pid':
        if not validate_pid(value):
            return False

    return True

def validate_byr(byr):
    if byr.isnumeric():
        if 1920 <= int(byr) <= 2002:
            return True
    return False


def validate_iyr(iyr):
    if iyr.isnumeric():
        if 2010 <= int(iyr) <= 2020:
            return True
    return False


def validate_eyr(eyr):
    if eyr.isnumeric():
        if 2020 <= int(eyr) <= 2030:
            return True
    return False


def validate_hgt(hgt):
    if hgt[-2:] == 'cm':
        if hgt[0:-2].isnumeric():
            if 150 <= int(hgt[0:-2]) <= 193:
                return True
    elif hgt[-2:] == 'in':
        if hgt[0:-2].isnumeric():
            if 59 <= int(hgt[0:-2]) <= 76:
                return True
    return False


def validate_hcl(hcl):
    if hcl[0] == '#':
        if len(hcl) == 7:
            if hcl[1:].isalnum():
                return True
    return False


def validate_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def validate_pid(pid):
    if pid.isnumeric():
        if len(pid) == 9:
            return True
    return False


if __name__ == '__main__':
    passports = get_passports("passports.txt")

    valid_ones = 0
    for passport in passports:
        if is_valid(passport):
            valid_ones += 1

    print(valid_ones)
