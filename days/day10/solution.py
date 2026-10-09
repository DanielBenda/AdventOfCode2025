from pathlib import Path

inside_cache = {}

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    bulbs = []
    buttons = []
    joltage = []
    for line in data:
        x, botjol = line.split("]")
        bulbs.append(x)
        y, z = botjol.split("{")
        buttons.append(y)
        joltage.append(z)

    bulbs = clean_bulbs(bulbs)

    print(bulbs, buttons, joltage)    

    result = "nothing"

    print(f"Day 10 - Part 1: {result}")

    print(f"Day 10 - Part 2: {result}")

def clean_bulbs(bulbs):
    for i in range(len(bulbs)):
        clean = bulbs[1][1:]
        bulbs[i] = clean
    return bulbs

def split_buttons(buttons):
    
    return buttons
