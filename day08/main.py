#!python3


def part1(path):
    with open(path) as f:
        data = [[int(y) for y in x[:-1]] for x in f.readlines()]
        visible = 0
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                v = True
                for x in range(0, i):
                    if data[x][j] >= data[i][j]:
                        v = False
                if v:
                    visible += 1
                    continue
                v = True
                for x in range(i + 1, len(data)):
                    if data[x][j] >= data[i][j]:
                        v = False
                if v:
                    visible += 1
                    continue
                v = True
                for x in range(0, j):
                    if data[i][x] >= data[i][j]:
                        v = False
                if v:
                    visible += 1
                    continue
                v = True
                for x in range(j + 1, len(data[i])):
                    if data[i][x] >= data[i][j]:
                        v = False
                if v:
                    visible += 1
                    continue
        visible += 2 * len(data) + 2 * len(data[0]) - 4
        return visible


def part2(path):
    with open(path) as f:
        data = [[int(y) for y in x[:-1]] for x in f.readlines()]
        result = []
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                a = 0
                b = 0
                c = 0
                d = 0
                for x in range(i-1, -1, -1):
                    a += 1
                    if data[x][j] >= data[i][j]:
                        break
                for x in range(i + 1, len(data)):
                    b += 1
                    if data[x][j] >= data[i][j]:
                        break
                for x in range(j - 1, -1, -1):
                    c += 1
                    if data[i][x] >= data[i][j]:
                        break
                for x in range(j + 1, len(data[i])):
                    d += 1
                    if data[i][x] >= data[i][j]:
                        break
                result.append(a * b * c * d)
        return max(result)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
