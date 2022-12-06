#!python3


def parse(path):
    with open(path) as f:
        raw_stacks = []
        moves = []
        top = True
        for line in f.readlines():
            if line.startswith(' 1') or line == '\n':
                top = False
                continue
            if top:
                raw_stacks.append(line)
            else:
                moves.append([int(x) for x in line[:-1].split(' ') if x.isnumeric()])
        raw_stacks.reverse()
        stack = [[] for _ in range(0, 11)]
        for line in raw_stacks:
            j = 1
            for i in range(1, len(line), 4):
                if line[i].isalpha():
                    stack[j].append(line[i])
                j += 1
        return moves, stack


def part1(path):
    moves, stack = parse(path)
    for move in moves:
        for i in range(move[0]):
            stack[move[2]].append(stack[move[1]].pop())
    res = ''
    for c in stack:
        if len(c) > 0:
            res = f'{res}{c[len(c) - 1]}'
    return res

def part2(path):
    moves, stack = parse(path)
    for move in moves:
        moved = [stack[move[1]].pop() for _ in range(move[0]) if len(stack[move[1]]) != 0]
        moved.reverse()
        for m in moved:
            stack[move[2]].append(m)
    res = ''
    for c in stack:
        if len(c) > 0:
            res = f'{res}{c[len(c) - 1]}'
    return res


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
