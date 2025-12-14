import sys
from importlib import import_module

def run_day(day: int):
    day_str = f"day{day:02d}"
    try:
        module = import_module(f"days.{day_str}.solution")
    except ModuleNotFoundError:
        print(f"❌ Day {day} not found")
        return

    if not hasattr(module, "solve"):
        print(f"❌ Day {day} has no solve() function")
        return

    module.solve()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
        sys.exit(1)

    run_day(int(sys.argv[1]))
