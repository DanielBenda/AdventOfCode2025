from pathlib import Path
from collections import Counter

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    coordinates = []
    for line in data:
        x, y, z = line.split(',')
        coordinates.append((int(x), int(y), int(z)))

    distances = []
    distances = find_distances(coordinates)
    distances = sorted(distances, key=lambda x: x[0])

    n = len(coordinates)
    representative = list(range(n)) 
    component_size = [1] * n             

    def find(node):
        if representative[node] != node:
            representative[node] = find(representative[node])
        return representative[node]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA == rootB:
            return False

        if component_size[rootA] < component_size[rootB]:
            rootA, rootB = rootB, rootA

        representative[rootB] = rootA
        component_size[rootA] += component_size[rootB]
        return True

    K = 1000
    connection = 0
    for distance, i, j in distances:
        union(i, j)  
        connection += 1
        if connection == K:
            break

    circuits = Counter()
    for i in range(n):
        boss = find(i)
        circuits[boss] += 1

    sizes = sorted(circuits.values(), reverse=True)
    counter = sizes[0] * sizes[1] * sizes[2]
    
    print(f"Day 08 - Part 1: {counter}")

    print(f"Day 08 - Part 2: {counter}")

def find_distances(coordinates):
    distances = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = compare_distance(coordinates[i], coordinates[j])
            distances.append((distance, i, j))  
    return distances

def compare_distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return x*x + y*y + z*z