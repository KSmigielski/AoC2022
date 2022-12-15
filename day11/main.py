#!python3
import operator
from math import gcd


def build_operation(operations_data):
    operation = operations_data[1]
    operand = None
    if operation == '+':
        operand = operator.add
    elif operation == '*':
        operand = operator.mul
    else:
        print(f'Unknown operator: f{operation}')
    if operations_data[2] == 'old':
        return lambda x: operand(x, x)
    else:
        return lambda x: operand(x, int(operations_data[2]))


def parse(path):
    with open(path) as f:
        lines = [x[:-1] for x in f.readlines()]
        i = 0
        monkeys = []
        while i < len(lines):
            i += 1
            monkey = {
                'checks': 0,
                'items': [int(x) for x in lines[i].replace('  Starting items: ', '').split(', ')]
            }
            i += 1
            monkey['operation'] = build_operation(lines[i].replace('  Operation: new = ', '').split(' '))
            i += 1
            monkey['test'] = int(lines[i].split(' ')[-1:][0])
            i += 1
            monkey['when_true'] = int(lines[i].split(' ')[-1:][0])
            i += 1
            monkey['when_false'] = int(lines[i].split(' ')[-1:][0])
            i += 2
            monkeys.append(monkey)
        return monkeys


def game(monkeys, r, sanity_check):
    for a in range(r):
        for m in monkeys:
            for i in m['items']:
                m['checks'] += 1
                new = sanity_check(m['operation'](i))
                new_monkey = -1
                if new % m['test'] == 0:
                    new_monkey = m['when_true']
                else:
                    new_monkey = m['when_false']
                monkeys[new_monkey]['items'].append(new)
            m['items'] = []
    checks = [m['checks'] for m in monkeys]
    checks.sort(reverse=True)
    return checks[0] * checks[1]


def part1(path):
    monkeys = parse(path)
    return game(monkeys, 20, lambda x: x // 3)


def lcm(a):
    lcm = 1
    for i in a:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def part2(path):
    monkeys = parse(path)
    div = lcm([x['test'] for x in monkeys])
    return game(monkeys, 10000, lambda x: x % div)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
