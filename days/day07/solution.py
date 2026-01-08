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
    
    print(f"Day 07 - Part 1: {counter}")

    counter = 0
    width = len(data[0])
    beams = [0] * width

    for line in data:
        for char in range(len(line)):
            if line[char] == 'S':
                beams[char] = 1
        new_beams = [0] * width
    
        for x in range(width):
            if beams[x] == 0:
                continue
        
            if line[x] == '^':
                new_beams[x-1] += beams[x]
                new_beams[x+1] += beams[x]
            else:
                new_beams[x] += beams[x]
    
        beams = new_beams
    counter = sum(beams)

    print(f"Day 07 - Part 2: {counter}")