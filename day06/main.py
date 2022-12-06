#!python3

def find_message(path, length):
    with open(path) as f:
        data = f.read()
        for i in range(length, len(data)):
            unique = set(data[i - length:i])
            if len(unique) == length:
                return i


def part1(path):
    return find_message(path, 4)


def part2(path):
    return find_message(path, 14)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
