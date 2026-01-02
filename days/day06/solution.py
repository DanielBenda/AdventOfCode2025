from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    counter = 0
    rows = []
    for line in data:
        row = [x for x in line.split(' ') if x != '']
        rows.append(row)

    columns = []
    for i in range(len(rows[0])):
        column = []
        for row in reversed(rows):
            column.append(row[i])
        columns.append(column)

    for column in columns:
        example = 0
        if column[0] == '+':
            for i in range(1, len(column)):
                example += int(column[i])
            counter += example
        if column[0] == '*':
            example = 1
            for i in range(1, len(column)):
                example = example * int(column[i])
            counter += example

    print(f"Day 06 - Part 1: {counter}")

    print(f"Day 06 - Part 2: {counter}")