def process_pass(pport):
    row, col = pport[:7], pport[-3:]
    row = int(row.replace('B', '1').replace('F','0'), 2)
    col = int(col.replace('R', '1').replace('L','0'), 2)
    return row * 8 + col

with open('input/day5.txt') as f:
    ans = [process_pass(passport.strip()) for passport in f.read().splitlines()]

print(ans)
print(max(ans), min(ans))
print(sum(range(59, 905)) - sum(ans))

