with open('input/day12.txt') as f:
    data = [line.strip() for line in f]
    data = [(line[0], int(line[1:])) for line in data] 

x = 0
y = 0
d = 'E'

dirs = ['N', 'E', 'S', 'W']
dirMap = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1)
}

def part1():
    def turn(dir, deg):
        if deg % 90 != 0:
            print(deg)
        global d
        if dir == 'L':
            d = dirs[(dirs.index(d)-deg//90)%4]
        else:
            print('ran', dirs.index(d))
            d = dirs[(dirs.index(d)+deg//90)%4]
        print('facing:', d)

    def theRest(dir, units):
        if dir == 'F':
            theRest(d, units)
        else:
            global x, y
            x += units * dirMap[dir][0]
            y += units * dirMap[dir][1]

    for cmd, units in data:
        if cmd in 'LR':
            turn(cmd, units)
        else:
            theRest(cmd, units)
        print(cmd, units, x, y)

    print(x, y)
    print(abs(x) + abs(y))

wx, wy = 1, 10
def part2():
    def theRest(dir, units):
        #nesw
        global wx, wy
        wx += units * dirMap[dir][0]
        wy += units * dirMap[dir][1]
    
    def forward(n):
        global x, y
        x += wx * n
        y += wy * n

    def left_wrap(deg):
        n = deg//90
        def left():
            global wx, wy
            wx, wy, = wy, -wx
        for _ in range(n):
            left()

    def right_wrap(deg):
        n = deg//90
        def right():
            global wx, wy
            wx, wy, = -wy, wx
        for _ in range(n):
            right()

    for cmd, units in data:
        if cmd in 'NSEW':
            theRest(cmd, units)
        elif cmd == 'L':
            left_wrap(units)
        elif cmd == 'R':
            right_wrap(units)
        elif cmd == 'F':
            forward(units)
        else:
            print('this should not happen')

    print(x, y, abs(x)+abs(y))

part2()

