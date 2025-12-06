import sys


def part1():
    def is_safe(report):
        decreasing = None

        for x, y in zip(report, report[1:]):
            if x == y or abs(x - y) > 3:
                return False

            if y < x:
                if decreasing is None:
                    decreasing = True
                elif not decreasing:
                    return False
            else:
                if decreasing is None:
                    decreasing = False
                elif decreasing:
                    return False

        return True
    
    reports = []

    for line in sys.stdin:
        reports.append([int(x) for x in line.strip().split()])

    return len([r for r in reports if is_safe(r)])


def part2():
    def is_safe_no_removals(report):
        decreasing = None

        for x, y in zip(report, report[1:]):
            if x == y or abs(x - y) > 3:
                return False

            if y < x:
                if decreasing is None:
                    decreasing = True
                elif not decreasing:
                    return False
            else:
                if decreasing is None:
                    decreasing = False
                elif decreasing:
                    return False

        return True


    reports = []
    number_safe = 0
    for line in sys.stdin:
        reports.append([int(x) for x in line.strip().split()])

    for report in reports:
        if is_safe_no_removals(report):
            number_safe += 1
        else:
            for to_remove_idx in range(len(report)):
                with_removed = report[:to_remove_idx] + report[to_remove_idx+1:]
                if is_safe_no_removals(with_removed):
                    number_safe += 1
                    break

    return number_safe


print(part2())
