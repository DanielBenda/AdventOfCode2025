from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    coordinates = []
    for line in data:
        x,y = line.split(",")
        coordinates.append((int(x), int(y)))  

    rectangles = find_rectangles(coordinates)
    rectangles = sorted(rectangles)
    result = rectangles[len(rectangles) -1]

    print(f"Day 09 - Part 1: {result}")

    print(f"Day 09 - Part 2: {result}")

def find_rectangles(coordinates):
    rectangles = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            rectangle = count_rectangle(coordinates[i], coordinates[j])
            rectangles.append((rectangle, i, j))  
    return rectangles

def count_rectangle(a, b):
    if a[0] >= b[0]:
        x = a[0] - b[0] + 1
    else:
        x = b[0] - a[0] + 1
    if a[1] >= b[1]:
        y = a[1] - b[1] + 1
    else: 
        y = b[1] - a[1] + 1
    return x * y
