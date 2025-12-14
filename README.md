# Advent of Code 2025 🎄🐍

This repository contains **my personal solutions** for  
[Advent of Code 2025](https://adventofcode.com/2025)  
a yearly programming challenge created by Eric Wastl.

The goal of this project is not just to get correct answers, but also to:
- practice problem solving
- experiment with clean Python project structure
- keep each day's solution isolated and easy to run
- have a bit of fun in December 🎅

---

## 🧠 Project Structure

Each Advent of Code day lives in its own folder and can be executed independently.

```text
AdventOfCode2025/
│
├─ main.py              # Central entry point for running solutions
├─ README.md
│
├─ days/
│  ├─ day01/
│  │  ├─ solution.py
│  │  └─ input.txt
│  ├─ day02/
│  │  ├─ solution.py
│  │  └─ input.txt
│  └─ ...
│
└─ .venv/               # Python virtual environment (not committed)

## ▶️ Running a Solution

All solutions are executed through main.py.

Run a specific day like this:

python main.py 1
python main.py 12


Each solution.py exposes a single solve() function which:

loads the input from input.txt

prints results for Part 1 and Part 2

Example output:

Day 01 - Part 1: 142
Day 01 - Part 2: 281