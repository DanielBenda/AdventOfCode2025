from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input()
    lines = data.splitlines()
    print(lines)
    joltage = 0

    for line in lines:
        firstNumber = 0
        index_1 = 0
        index_2 = 0
        secondNumber = 0
        result = 0
        for i, ch in enumerate(line):
            index_2 = index_2 + 1
            index_1 = i
            firstNumber = int(line[i])

            for i, ch in enumerate(line[index_2:], start=index_2):
                secondNumber = int(ch)
                if int(str(firstNumber) + str(secondNumber)) > result:
                    if index_1 != index_2:
                        result = int(str(firstNumber) + str(secondNumber))
         
        print(result)
        joltage = joltage + result

    
    # part 1
    print(f"Day 01 - Part 1: {joltage}")


    # part 2
    print(f"Day 01 - Part 2: {joltage}")
