#!python3

from collections import defaultdict


def find_commons(parts):
    data = defaultdict(lambda: 0)
    for part in parts:
        for char in set(list(part)):
            data[char] += 1
    return data


def calculate_priority(data, n):
    s = 0
    for k, v in data.items():
        if v == n:
            if k.islower():
                s += ord(k) - 96
            else:
                s += ord(k) - 38
    return s


def split_into_parts(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def split_into_chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def part1(path):
    with open(path) as f:
        return sum([calculate_priority(find_commons(split_into_parts(x, 2)), 2) for x in
                    [x[:-1] for x in f.readlines()]])


def part2(path):
    with open(path) as f:
        return sum([calculate_priority(find_commons(x), 3) for x in split_into_chunks([x[:-1] for x in f.readlines()], 3)])


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
