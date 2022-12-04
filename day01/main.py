#!python3


def sum_top(path, n):
    with open(path) as f:
        table = list(map(lambda x: sum([int(y) for y in x.split('\n') if y != '']), f.read().split('\n\n')))
        table.sort()
        return sum(table[-n:])


def part1(path):
    return sum_top(path, 1)


def part2(path):
    return sum_top(path, 3)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
