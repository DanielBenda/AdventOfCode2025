from pathlib import Path

def load_input() -> str:
    return Path(__file__).with_name("input.txt").read_text().strip()


def solve():
    data = load_input().split(",")
    ranges = []
    for item in data:
        start, end = map(int, item.split("-"))
        ranges.append((start, end))

    counter = 0
    for start, end in ranges:
        for j in range(start, end + 1):
            s = str(j)
            if j > 9 :
                a, b = int(s[:len(s)//2]), int(s[len(s)//2:])
            if len(s) % 2 == 0:
                if a == b:
                    counter = counter + j
                        
    # part 1
    result_1 = counter
    print(f"Day 02 - Part 1: {result_1}")

    counter = 0
    for start, end in ranges:
        for j in range(start, end + 1):
            s = str(j)
            #print("proslo: ", j)
            if j > 9 :
                splits = all_possible_splits(j)
                for k, parts in splits.items():
                    if len(set(parts)) == 1:
                        counter = counter + j
                        break
    # part 2
    result_2 = counter
    print(f"Day 02 - Part 2: {result_2}")

def all_possible_splits(n):
    s = str(n)
    L = len(s)
    results = {}

    for k in range(2, L + 1):
        if L % k == 0:
            size = L // k
            parts = [int(s[i:i+size]) for i in range(0, L, size)]
            results[k] = parts

    return results
