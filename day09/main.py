#!python3
from collections import defaultdict


def move_head(head, direction):
    if direction == 'L':
        return head[0], head[1] - 1
    if direction == 'R':
        return head[0], head[1] + 1
    if direction == 'U':
        return head[0] + 1, head[1]
    if direction == 'D':
        return head[0] - 1, head[1]


def clamp(num):
    return max(min(num, 1), -1)


def move_to_target(target, knot):
    delta_x = target[1] - knot[1]
    delta_y = target[0] - knot[0]
    if abs(delta_y) < 2 and abs(delta_x) < 2:
        delta_y = 0
        delta_x = 0
    else:
        delta_x = clamp(delta_x)
        delta_y = clamp(delta_y)
    return knot[0] + delta_y, knot[1] + delta_x


def path_finding(path, n):
    with open(path) as f:
        positions = defaultdict(lambda: 0)
        knots = [(0, 0) for _ in range(n)]
        positions[(0, 0)] += 1
        for line in [x[:-1] for x in f.readlines()]:
            split = line.split(' ')
            direction = split[0]
            delta = int(split[1])
            for i in range(delta):
                knots[0] = move_head(knots[0], direction)
                for k in range(1, n):
                    target = knots[k - 1]
                    knot = knots[k]
                    knots[k] = move_to_target(target, knot)
                positions[knots[n - 1]] = 1
        return sum(positions.values())


def part1(path):
    return path_finding(path, 2)


def part2(path):
    return path_finding(path, 10)


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
