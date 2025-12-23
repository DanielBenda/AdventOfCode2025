from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()

def solve():
    data = load_input()
    lines = [list(line) for line in data.splitlines()]    
    rolls = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '@':
                if find_adjacent(lines, x, y):
                    rolls += 1     
    
    print(f"Day 01 - Part 1: {rolls}")

    lines = [list(line) for line in data.splitlines()]    
    rolls = 0
    while True:
        moreRoles = 0
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == '@':
                    if find_adjacent(lines, x, y):
                        moreRoles += 1 
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == 'x':
                    lines[y][x] = '.'

        rolls = rolls + moreRoles
        if moreRoles == 0:
            break

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
            if grid[ny][nx] == '@' or grid[ny][nx] == 'x':
                adjacent_rolls += 1
            pass
    if adjacent_rolls <= 3:
        grid[y][x] = 'x'

    return adjacent_rolls <= 3
