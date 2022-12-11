#!python3


def part1(path):
    with open(path) as f:
        result = []
        cycle = 1
        register = 1
        for data in [x[:-1].split(' ') for x in f.readlines()]:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                result.append(cycle * register)
            if len(data) == 2:
                cycle += 1
                register += int(data[1])
                if (cycle - 20) % 40 == 0:
                    result.append(cycle * register)
        return sum(result)



def part2(path):
    with open(path) as f:
        result = []
        cycle = 1
        register = 1
        row = 0
        result.append([])
        for data in [x[:-1].split(' ') for x in f.readlines()]:
            if cycle % 41 in range(register, register + 3):
                result[row].append('#')
            else:
                result[row].append('.')
            cycle += 1
            if cycle % 41 == 0:
                row += 1
                cycle = 1
                result.append([])
            if len(data) == 2:
                if cycle % 41 in range(register, register + 3):
                    result[row].append('#')
                else:
                    result[row].append('.')
                cycle += 1
                register += int(data[1])
                if cycle % 41 == 0:
                    row += 1
                    cycle = 1
                    result.append([])

        return '\n'.join(map(''.join, result))


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2:\n{part2(test_data)}')
    print(f'part 2:\n{part2(data)}')
