from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input()
    lines = data.splitlines()
    print(lines)
    rolls = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '@':
                if find_adjacent(lines, x, y):
                    rolls += 1     
    
    print(f"Day 01 - Part 1: {rolls}")

    print(f"Day 01 - Part 2: {rolls}")

def find_adjacent(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1,  0), (1,  0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]

    adjacent_rolls = 0

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= ny < rows and 0 <= nx < cols:
            if grid[ny][nx] == '@':
                adjacent_rolls += 1
            pass

    return adjacent_rolls <= 3
