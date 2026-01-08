from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().splitlines()
    counter = 0
    beams = []
    for line in data: 
        for char in range(len(line)):
            if line[char] == 'S':
                beams.append(char)
            if line[char] == '^' and beams.__contains__(char):
                beams.append(char - 1)
                beams.append(char + 1)
                while beams.__contains__(char):
                    beams.remove(char)
                counter += 1
        print(beams)        
    
    print(f"Day 07 - Part 1: {counter}")

    print(f"Day 07 - Part 2: {counter}")