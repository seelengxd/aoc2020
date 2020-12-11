from collections import Counter

with open('input/day10.txt') as f:
    data = list(map(int, f.read().strip().split()))
    data.append(0)
    data.append(max(data)+3)

data.sort()

#part 1
print(data)
counted = Counter([data[i+1]-data[i]for i in range(len(data)-1)])
print(counted[1]*counted[3])

#part2

table = [0] * (max(data)+1) 
table[0] = 1 #base case
for i in data:
    prev = (i-1, i-2, i-3)
    for j in prev:
        if j >= 0:
            table[i] += table[j]

print(table[-1])
