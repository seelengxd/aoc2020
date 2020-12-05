import re
with open('input/day4.txt') as f:
    data = f.read().split('\n\n')


ans = 0

# required = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid', 'hcl'] 
# for line in data:
#     ans += all(req+':' in line for req in required)

for passport in data:
    passport += ' '
    try:
        #byr
        byr = re.search('byr:(\d{4})\s', passport)
        if not byr:
            raise ValueError('no byr')
        byr = byr.group(1)
        assert 1920 <= int(byr) <= 2002, 'byr not in range'

        #iyr
        iyr = re.search('iyr:(\d{4})\s', passport)
        if not iyr:
            raise ValueError('no iyr')
        iyr = iyr.group(1)
        assert 2010 <= int(iyr) <= 2020, 'iyr not in range' 

        #iyr
        eyr = re.search('eyr:(\d{4})\s', passport)
        if not eyr:
            raise ValueError('no eyr')
        eyr = eyr.group(1)  
        assert 2020 <= int(eyr) <= 2030, 'eyr not in range'  

        #hgt
        hgt = re.search('hgt:(\d+)cm\s', passport)
        if hgt:
            assert 150 <= int(hgt.group(1)) <= 193
        else:
            hgt = re.search('hgt:(\d+)in\s', passport)
            assert 59 <= int(hgt.group(1)) <= 76

        #hcl
        hcl = re.search('hcl:#[0-9a-f]{6}\s', passport)
        assert hcl is not None

        #ecl
        ecl = re.search('ecl:([a-z]{3})\s', passport).group(1)
        assert ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        #pid
        assert re.search('pid:\d{9}\s', passport) is not None

        ans += 1

    except Exception as e:
        # print(e)
        pass
    else:
        # print(passport, end="\n\n")
    

print(ans)
