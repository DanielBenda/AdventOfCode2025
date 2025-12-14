from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input()
    lines = data.splitlines()
    parsed = [(line[0], int(line[1:])) for line in lines]

    pointer = 50 
    counter = 0

    for direction, step in parsed:
        if step > 99:
            step = step % 100
        if direction == 'L':
            if step >= pointer:
                pointer = pointer + 100
                pointer = pointer - step
            else:
                pointer = pointer - step    
        elif direction == 'R':
            pointer = pointer + step
        else:
            print(f"Unknown direction {direction}")
        if pointer > 99:
            pointer = pointer - 100
        print(pointer)
        if pointer == 0:
            counter = counter + 1

    # part 1
    result_1 = counter
    print(f"Day 01 - Part 1: {result_1}")

    # part 2
    result_2 = sum(len(line) for line in lines)
    print(f"Day 01 - Part 2: {result_2}")
