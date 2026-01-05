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

    counter = 0

    operators = [c for c in data[-1] if c in '+*']

    data = [line + ' ' for line in data]

    line_max_length = max(len(x) for x in data)

    for line in data:
        if len(line) < line_max_length:
            line = line + ' '
    
    line1 = data[0]
    line2 = data[1]
    line3 = data[2]
    line4 = data[3]

    line1_numbers = []
    line2_numbers = []
    line3_numbers = []
    line4_numbers = []

    current_position = 0

    for i in range(len(line1)):
        if line1[i] == ' ' and line2[i] == ' ' and line3[i] == ' ' and line4[i] == ' ':
            line1_numbers.append(line1[current_position:i])
            line2_numbers.append(line2[current_position:i])
            line3_numbers.append(line3[current_position:i])
            line4_numbers.append(line4[current_position:i])
            current_position = i + 1 

    for column in range(len(line1_numbers)):    
        nums = []
        digit_chars = []
        num1 = line1_numbers[column]
        num2 = line2_numbers[column]
        num3 = line3_numbers[column]
        num4 = line4_numbers[column]
        for col_idx in range(len(num1)):
            digit_chars = []
            if num1[col_idx].isdigit:
                digit_chars.append(num1[col_idx])
            if num2[col_idx].isdigit:
                digit_chars.append(num2[col_idx])    
            if num3[col_idx].isdigit:
                digit_chars.append(num3[col_idx])   
            if num4[col_idx].isdigit:
                digit_chars.append(num4[col_idx]) 
            if digit_chars:
                nums.append(int(''.join(digit_chars)))

        op = operators[column]
        if op == '+':
            result = sum(nums) 
        else:
            result = 1
            for n in nums:
                result *= n
        counter += result

    print(f"Day 06 - Part 2: {counter}")
