#!python3
from itertools import product


def calculate_score(path, table):
    with open(path) as f:
        return sum(list(map(lambda x: table[x], [tuple(x[:-1].split(' ')) for x in f.readlines()])))


def part1(path):
    table = {
        ('A', 'X'): 3 + 1,
        ('A', 'Y'): 6 + 2,
        ('A', 'Z'): 0 + 3,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 6 + 1,
        ('C', 'Y'): 0 + 2,
        ('C', 'Z'): 3 + 3
    }
    return calculate_score(path, table)


def part2(path):
    table = {
        ('A', 'X'): 0 + 3,
        ('A', 'Y'): 3 + 1,
        ('A', 'Z'): 6 + 2,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 0 + 2,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 6 + 1
    }
    return calculate_score(path, table)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
