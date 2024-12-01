from collections import defaultdict
from aoc_api import get_input, submit

def part1():
    lines = get_input(1)
    lefts = map(
        lambda line: int(line.split()[0].strip()),
        sorted(lines, key=lambda line: int(line.split()[0].strip())))
    rights = map(
        lambda line: int(line.split()[1].strip()),
        sorted(lines, key=lambda line: int(line.split()[1].strip())))

    result = sum(map(lambda x: abs(x[0] - x[1]), zip(lefts, rights)))

    submit(day=1, level=1, answer=result, really=True)


def part2():
    lines = get_input(1)

    lefts = map(lambda line: int(line.split()[0].strip()), lines)
    rights = map(lambda line: int(line.split()[1].strip()), lines)
    counts = defaultdict(int)
    for entry in rights:
        counts[entry] += 1

    result = 0
    for entry in lefts:
        result += entry * counts[entry]

    submit(day=1, level=2, answer=result, really=True)

part2()
