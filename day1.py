import sys
from collections import defaultdict


def part1():
    left, right = [], []
    for line in sys.stdin:
        x, y = line.split()
        x = int(x)
        y = int(y)
        left.append(x)
        right.append(y)

    left = sorted(left)
    right  = sorted(right)

    result = 0
    for i in range(len(left)):
        result += abs(right[i] - left[i])

    return result


def part2():
    left, right = [], []
    for line in sys.stdin:
        x, y = line.split()
        x = int(x)
        y = int(y)
        left.append(x)
        right.append(y)    

    result = 0
    for left_number in left:
        count = len(list(filter(lambda x: x == left_number, right)))
        result += left_number * count

    return result


print(part2())
