from aocd import data
data = data.split('\n\n')
for i in range(len(data)):
    data[i] = data[i].replace('\n', ' ').strip()

passport_information = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def passport_check(passport: dict):
    required_fields = 0
    required_fields = 0
    for key in passport_information:
        if key in passport:
            required_fields += 1
    if required_fields == 7:
        return True
    return False


def passport_strict(passport):
    hgt = int(str(0) + passport.get("hgt")[:-2])
    cmin = passport.get("hgt")[-2:]
    if not 1920 <= int(passport.get("byr")) <= 2002:
        return False
    if not 2010 <= int(passport.get("iyr")) <= 2020:
        return False
    if not 2020 <= int(passport.get("eyr")) <= 2030:
        return False
    if passport.get("ecl") not in eyeColor:
        return False
    if len(passport.get("pid")) != 9:
        return False
    if len(passport.get("hcl")) != 7:
        return False
    if cmin == "cm":
        if not 150 <= hgt <= 193:
            return False
    elif cmin == "in":
        if not 59 <= hgt <= 76:
            return False
    else:
        return False
    return True


valid_passports = 0
strict_passports = 0

for i in range(len(data)):
    passport_data = dict(x.split(":") for x in data[i].split(" "))
    passport_valid = passport_check(passport_data)
    valid_passports += passport_valid
    if passport_valid:
        passport_valid = passport_strict(passport_data)
        strict_passports += passport_valid

print(valid_passports)
print(strict_passports)
