with open('input/day3.txt') as f:
    grid = [line.strip() for line in f]

def check(right, down):
    row = len(grid[0])
    col = len(grid)
    ans = 0
    i = 0
    while i * down < col:
        ans += (grid[i*down][i*right%row] == '#')
        i += 1
    return ans

print(len(grid))
print(check(3, 1))
print(check(1, 1) * check(3, 1) * check(5, 1) * check(7, 1)  * check(1, 2))