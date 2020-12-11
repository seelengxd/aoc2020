import copy

with open('input/day11.txt') as f:
    data = [list(line.strip()) for line in f]
    prev = copy.deepcopy(data)

rows, cols = len(data), len(data[0])

def access(x, y):
    if 0 <= x < rows and 0 <= y < cols:
        return prev[x][y]
    else:
        return None

def traverse(x, y, i, j, first=False):
    if first or access(x, y) == '.':
        return traverse(x+i, y+j, i, j)
    else:
        return access(x, y)

TOLERANCE = 5

test = 0 
while True:
    test += 1
    change = False
    for i in range(rows):
        for j in range(cols):
            # part 1
            # adjacent = [access(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) if (x, y) != (i, j)]
            adjacent = [traverse(i, j, x, y, True) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]
            curr = prev[i][j]

            if curr == 'L' and '#' not in adjacent:
                data[i][j] = '#' 
                change = True
            elif curr == '#' and adjacent.count('#') >= TOLERANCE:
                data[i][j] = 'L'
                change = True
    
    if not change:
        break
    else:
        prev = copy.deepcopy(data)

print(sum([line.count('#') for line in data]))
print(test)