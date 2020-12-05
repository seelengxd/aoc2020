import re

def p1():
    count = 0 
    with open('input/day2.txt') as f:
        for line in f:
            data = re.search('(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)', line.strip()).group()
            low, high, letter, pw  = data
            low, high = int(low), int(high)
            count += (low <= pw.count(letter) <= high)

    print(count)

def p2():
    count = 0
    with open('input/day2.txt') as f:
        for line in f:
            data = re.findall('(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)', line.strip())[0]
            low, high, letter, pw  = data
            low, high = int(low)-1, int(high)-1
            count += ((pw[low] == letter) ^ (pw[high] == letter))

    print(count)

p2()


#5-6 b: bbbbhzbz