from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    ranges = []
    values = []
    for item in data:
        if '-' in item:
            start, end = map(int, item.split("-"))
            ranges.append((start, end))
        elif not item:
            continue
        else: 
            values.append(int(item))

    counter = 0
    for j in values:
        for start, end in ranges:
            if start <= j <= end:
                counter += 1
                break
    
    print(f"Day 05 - Part 1: {counter}")

    counter = 0

    print(f"Day 05 - Part 2: {counter}")