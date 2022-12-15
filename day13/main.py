#!python3
import ast
from functools import cmp_to_key


def check(a, b):
    for i, j in zip(range(len(a)), range(len(b))):
        if type(a[i]) is list or type(b[j]) is list:
            left = a[i] if type(a[i]) is list else [a[i]]
            right = b[j] if type(b[j]) is list else [b[j]]
            value = check(left, right)
            if value != 0:
                return value
            else:
                continue
        else:
            left = a[i]
            right = b[i]
            if left < right:
                return 1
            elif left > right:
                return -1
            else:
                continue
    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        return 0


def part1(path):
    with open(path) as f:
        lines = f.read().splitlines()
        results = []
        i = 0
        while i < len(lines):
            a = ast.literal_eval(lines[i])
            b = ast.literal_eval(lines[i + 1])
            results.append(check(a, b))
            i += 3
        return sum([x + 1 for x, y in enumerate(results) if y == 1])


def part2(path):
    with open(path) as f:
        lines = [x for x in f.read().splitlines() if x != '']
        results = [
            [[2]],
            [[6]]
        ]
        for line in lines:
            results.append(ast.literal_eval(line))
        results.sort(key=cmp_to_key(check), reverse=True)
        r = [x + 1 for x, y in enumerate(results) if y in [[[2]], [[6]]]]
        return r[0] * r[1]


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
