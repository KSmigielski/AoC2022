#!python3
from collections import defaultdict


def parse(path):
    with open(path) as f:
        paths = list(map(lambda x: list(map(lambda y: tuple(map(int, y.split(','))), x.split(' -> '))),
                         [x[:-1] for x in f.readlines()]))
        roof = defaultdict(lambda: 0)
        for path in paths:
            for i in range(1, len(path)):
                a = path[i - 1]
                b = path[i]
                if a[0] == b[0]:
                    for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                        roof[(a[0], j)] = 1
                else:
                    for j in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                        roof[(j, a[1])] = 1
        return roof


def simulate(roof, test):
    drop = False
    count = -1
    while not drop:
        count += 1
        possible_sand = (500, 0)
        while True:
            org_sand = possible_sand
            possible_sand = (possible_sand[0], possible_sand[1] + 1)
            if test(possible_sand):
                drop = True
                break
            if roof[possible_sand] == 0:
                continue
            if roof[(possible_sand[0] - 1, possible_sand[1])] == 0:
                possible_sand = (possible_sand[0] - 1, possible_sand[1] - 1)
                continue
            if roof[(possible_sand[0] + 1, possible_sand[1])] == 0:
                possible_sand = (possible_sand[0] + 1, possible_sand[1] - 1)
                continue
            roof[org_sand] = 1
            break
    return count


def part1(path):
    roof = parse(path)
    m_y = max(map(lambda x: x[1], roof.keys()))
    return simulate(roof, lambda x: x[1] == m_y + 1)


def part2(path):
    roof = parse(path)
    m_y = max(map(lambda x: x[1], roof.keys())) + 2
    min_x = min(map(lambda x: x[0], roof.keys()))
    max_x = max(map(lambda x: x[0], roof.keys())) + 1
    for i in range(min_x - m_y, max_x + m_y):
        roof[(i, m_y)] = 1
    return simulate(roof, lambda x: roof[(500, 0)] == 1)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
