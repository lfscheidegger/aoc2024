import sys
import re

regex = re.compile('mul\\((\\d{1,3}),(\\d{1,3})\\)')


def part1():
    result = 0
    
    for line in sys.stdin:
        for m in regex.findall(line):
            result += int(m[0]) * int(m[1])
        
    return result


def part2():
    result = 0
    regex = re.compile('(mul\\((\\d{1,3}),(\\d{1,3})\\))|(do\\(\\))|(don\'t\\(\\))')

    enabled = True
    for line in sys.stdin:
        for m in regex.findall(line):
            if m[3]:
                enabled = True
            elif m[4]:
                enabled = False
            elif enabled:
                result += int(m[1]) * int(m[2])
        
    return result    


print(part2())
