#!python3
from queue import PriorityQueue
import math

neighbour_dir = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjacency_matrix = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1


def dijkstra(graph, start_vertex):
    d = {v: math.inf for v in range(graph.num_of_vertices)}
    d[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.num_of_vertices):
            if graph.adjacency_matrix[current_vertex][neighbor] != -1:
                distance = graph.adjacency_matrix[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = d[neighbor]
                    new_cost = d[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        d[neighbor] = new_cost
    return d


def build_graph(path, add_vertex):
    with open(path) as f:
        lines = [x[:-1] for x in f.readlines()]
        start = None
        end = None
        width = len(lines[0])
        height = len(lines)
        vertices = []
        lowest_points = []

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                elevation = None
                idx = len(vertices)
                if c == 'S':
                    elevation = 0
                    start = idx
                elif c == 'E':
                    elevation = ord('z') - 97
                    end = idx
                else:
                    elevation = ord(c) - 97

                if elevation == 0:
                    lowest_points.append(idx)

                vertices.append(elevation)

        graph = Graph(len(vertices))
        for idx, elevation in enumerate(vertices):
            y = int(idx / width)
            x = int(idx % width)
            for nd in neighbour_dir:
                nx = x + nd[0]
                ny = y + nd[1]
                if nx < 0 or ny < 0 or nx >= width or ny >= height:
                    continue

                nidx = nx + (ny * width)
                ne = vertices[nidx]

                if (elevation + 1) >= ne:
                    add_vertex(graph, idx, nidx)
        return start, end, graph, lowest_points


def part1(path):
    start, end, graph, _ = build_graph(path, lambda graph, idx, nidx: graph.add_edge(idx, nidx))
    return dijkstra(graph, start)[end]


def part2(path):
    start, end, graph, lowest_points = build_graph(path, lambda graph, idx, nidx: graph.add_edge(nidx, idx))
    d = dijkstra(graph, end)
    return min(map(lambda x: d[x], lowest_points))


if __name__ == '__main__':
    test_data = 'test_input.txt'
    data = 'input.txt'

    print(f'test part 1: {part1(test_data)}')
    print(f'part 1: {part1(data)}')
    print(f'test part 2: {part2(test_data)}')
    print(f'part 2: {part2(data)}')
