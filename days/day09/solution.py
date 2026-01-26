from pathlib import Path

inside_cache = {}

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

    rectangles = find_rectangles_in_polygon(coordinates)

    print(f"Day 09 - Part 2: {rectangles[0]}")

def find_rectangles(coordinates):
    rectangles = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            rectangle = count_rectangle(coordinates[i], coordinates[j])
            rectangles.append((rectangle, i, j))  
    return rectangles

def find_rectangles_in_polygon(coordinates):
    n = len(coordinates)

    candidates = []

    for i in range(n):
        x1, y1 = coordinates[i]
        for j in range(i+1, n):
            x2, y2 = coordinates[j]
            area = count_rectangle((x1, y1), (x2, y2))

            if area <= 0:
                continue

            candidates.append((area, i, j))
    candidates.sort(reverse=True)

    for area, i, j in candidates:
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]

        if rectangle_fits(coordinates, x1, y1, x2, y2):
            return [(area, i, j)]

    return []

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

def point_in_polygon_cached(x, y, poly):
    key = (x, y)
    if key in inside_cache:
        return inside_cache[key]

    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if ((y1 > y) != (y2 > y)):
            x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x_intersect > x:
                inside = not inside

    inside_cache[key] = inside
    return inside

def rectangle_fits(polygon, x1, y1, x2, y2):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)

    if maxx - minx <= 0 or maxy - miny <= 0:
        return False

    EPS = 1e-6

    cx = (minx + maxx) * 0.5
    cy = (miny + maxy) * 0.5
    if not point_in_polygon_cached(cx, cy, polygon):
        return False

    corners = [
        (minx + EPS, miny + EPS),
        (maxx - EPS, miny + EPS),
        (minx + EPS, maxy - EPS),
        (maxx - EPS, maxy - EPS),
    ]

    for (x, y) in corners:
        if not point_in_polygon_cached(x, y, polygon):
            return False

    for x in range(minx, maxx):
        if not point_in_polygon_cached(x + 0.5, miny + EPS, polygon):
            return False
        if not point_in_polygon_cached(x + 0.5, maxy - EPS, polygon):
            return False

    for y in range(miny, maxy):
        if not point_in_polygon_cached(minx + EPS, y + 0.5, polygon):
            return False
        if not point_in_polygon_cached(maxx - EPS, y + 0.5, polygon):
            return False

    return True