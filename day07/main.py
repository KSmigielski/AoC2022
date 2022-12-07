#!python3

def new_file(name, size):
    return {
        "name": name,
        "type": "file",
        "size": size
    }


def new_dir(name):
    return {
        "name": name,
        "type": "dir",
        "childes": [],
        'size': 0
    }


def dir_size(dir):
    s = 0
    for c in dir['childes']:
        if c == 'file':
            s += c['size']
        elif c['size'] != 0:
            s += c['size']
        else:
            c['size'] = dir_size(c)
            s += c['size']
    dir['size'] = s
    return s


def add_element(element, path, root):
    current = root
    for path_part in path[1:]:
        for child in current['childes']:
            if child['name'] == path_part and child['type'] == 'dir':
                current = child
                break
    current['childes'].append(element)


def traverse(root, data):
    for e in root['childes']:
        if e['type'] == 'dir':
            traverse(e, data)
    s = dir_size(root)
    data.append(s)


def parse(path):
    with open(path) as f:
        root = new_dir('/')
        path = ['/']
        for line in [x[:-1] for x in f.readlines()]:
            if line.startswith('$'):
                data = line.split(' ')
                if data[1] == 'cd':
                    if data[2] == '/':
                        path = ['/']
                    elif data[2] == '..':
                        path.pop()
                    else:
                        path.append(data[2])
            else:
                data = line.split(' ')
                element = None
                if data[0] == 'dir':
                    element = new_dir(data[1])
                else:
                    element = new_file(data[1], int(data[0]))
                add_element(element, path, root)
    return root


def part1(path):
    root = parse(path)
    data = []
    traverse(root, data)
    return sum([x for x in data if x <= 100000])



def part2(path):
    root = parse(path)
    data = []
    traverse(root, data)
    unused_space = 70000000 - root['size']
    return min([x for x in data if unused_space + x >= 30000000])


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
