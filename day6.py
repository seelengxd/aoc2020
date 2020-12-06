from pprint import pprint

with open('input/day6.txt') as f:
    data = [line.split('\n') for line in f.read().strip().split('\n\n')]
    data = [[set(ans) for ans in group] for group in data]

processed = []
for group in data:
    temp = set(group[0])
    for x in group[1:]:
        temp = temp.intersection(set(x))
    processed.append(temp)

pprint(processed)
pprint(sum(len(i) for i in ))