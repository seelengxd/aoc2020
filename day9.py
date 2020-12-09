def find_pair(L, t):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] + L[j] == t:
                return True
    return False

with open('input/day9.txt') as f:
    data = list(map(int, f.read().strip().split('\n')))

for i in range(25, len(data)):
    if not find_pair(data[:i], data[i]):
        part1 = data[i]
        break

#part 2 --> kind of similar to kadane's algo

curr = data[0]
# contig = [curr]
currSum = curr
currNext = 1
currFront = 0
while currSum != part1:
    while currSum < part1:
        currSum += data[currNext]
        currNext += 1
    while currSum > part1:
        currSum -= data[currFront]
        currFront += 1

res = data[currFront:currNext]
print(min(res) + max(res))



