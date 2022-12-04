#!python3

def parse_groups(v):
    return list(map(lambda x: list(map(int, x.split('-'))), v))


def is_subset(v):
    a = v[0]
    b = v[1]
    a_set = set(range(a[0], a[1] + 1))
    b_set = set(range(b[0], b[1] + 1))
    if a_set.issubset(b_set):
        return 1
    elif b_set.issubset(a_set):
        return 1
    else:
        return 0


def is_overlapping(v):
    a = v[0]
    b = v[1]
    a_set = set(range(a[0], a[1] + 1))
    b_set = set(range(b[0], b[1] + 1))
    if len(a_set.intersection(b_set)) == 0:
        return 0
    else:
        return 1


def part1(path):
    with open(path) as f:
        return sum(map(is_subset, map(parse_groups, [x[:-1].split(',') for x in f.readlines()])))


def part2(path):
    with open(path) as f:
        return sum(map(is_overlapping, map(parse_groups, [x[:-1].split(',') for x in f.readlines()])))


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
