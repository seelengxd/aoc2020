# import copy

def read():
    with open('input/day8.txt') as f:
        commands = [i.split() for i in f.read().strip().split('\n')]
        commands = [(command, int(number)) for command, number in commands]
    return commands

read()


def process(commands):
    ran = []
    curr = 0
    acc = 0

    while curr not in ran:
        ran.append(curr)

        if curr == len(commands)-1:
            print('test', end=" ")
            print(acc)

        command, number = commands[curr]

        # print(curr, command, number)

        if command == 'jmp':
            curr += number
        else:
            if command == 'acc':
                acc += number
            curr += 1

        if curr == len(commands):
            print(acc)
            break
        
        

commands = read()
jmps = [i for i in range(len(commands)) if commands[i][0] == 'jmp']
nops = [i for i in range(len(commands)) if commands[i][0] == 'nop']

for i in jmps:
    to_change = read()
    to_change[i] = ('nop', to_change[i][1])
    # print(to_change[0])
    process(to_change)

for i in nops:
    to_change = read()
    to_change[i] = ('jmp', to_change[i][1])
    process(to_change)