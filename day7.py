import re


def part1():
    with open('input/day7.txt') as f:
        data = [re.findall('([a-zA-Z]+ [a-zA-Z]+) bag', line) for line in f]
        #bag: [other bags]
        processed = {i[0]: i[1:] if i[1:] != ['no other'] else [] for i in data}

    table = {}
    def check_bag(bag, target):
        #memoize
        if bag in table:
            return table[bag]
        else:
            res = target in processed[bag] or any(check_bag(b, target) for b in processed[bag])
            table[bag] = res
            return res

    count = 0
    for bag in processed:
        count += check_bag(bag, 'shiny gold')

    print(count)


def part2():
    with open('input/day7.txt') as f:
        data = [re.findall('^([a-zA-Z]+ [a-zA-Z]+) bag', line) + re.findall('(\d+) ([a-zA-Z]+ [a-zA-Z]+) bag', line) for line in f]
        #bag: [other bags in the form (bag, count)]
        processed = {i[0]: i[1:] if i[1:] != ['no other'] else [] for i in data}
        for k, v in processed.items():
            processed[k] = [(j, int(i)) for i, j in v]

    table = {}
    def check_bag(bag):
        #memoize
        if bag in table:
            return table[bag]
        else:
            #how many indiv bags + how many bags in those bags
            res = sum(i[1] for i in processed[bag]) + sum(v * check_bag(b) for b, v in processed[bag])
            table[bag] = res
            return res

    count = check_bag('shiny gold')
    print(count)
    # print(table)
    for k in table:
        print(k, processed[k])

part2()