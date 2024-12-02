from pathlib import Path
from collections import Counter


def load_input(path: Path) -> tuple[list[int], list[int]]:
    lines = path.read_text().splitlines()
    left = []
    right = []
    for line in lines:
        [l, r] = line.split()
        left.append(int(l))
        right.append(int(r))
    return left, right


def part_a(path: Path):
    left, right = load_input(path)
    left.sort()
    right.sort()
    distances = [abs(l - r) for (l, r) in zip(left, right)]
    print("Part A -- Answer: ", sum(distances))


def part_b(path: Path):
    left, right = load_input(path)
    frequencies = Counter(right)
    scores = [x * frequencies.get(x, 0) for x in left]
    print("Part B -- Answer: ", sum(scores))


def main():
    print("Day 01")
    part_a(Path("inputs/day01_test.txt"))
    part_a(Path("inputs/day01.txt"))
    part_b(Path("inputs/day01_test.txt"))
    part_b(Path("inputs/day01.txt"))


if __name__ == "__main__":
    main()
