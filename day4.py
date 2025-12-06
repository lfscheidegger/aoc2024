import sys


def part1():
    grid = [line.strip() for line in sys.stdin]
    height = len(grid)
    width = len(grid[0])
    
    def try_it(x, y):
        deltas = [
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0],
            [-1, -1],
            [0, -1],
            [1, -1]
        ]

        result = 0

        for delta in deltas:
            xx = x
            yy = y
            found = 1
            for test_letter in 'XMAS':
                if xx < 0 or xx >= width or yy < 0 or yy >= height:
                    found = 0
                    break

                if grid[yy][xx] != test_letter:
                    found = 0
                    break

                xx += delta[0]
                yy += delta[1]

            result += found

        return result


    result = 0
    for y in range(height):
        for x in range(width):
            letter = grid[y][x]
            if letter != 'X':
                continue

            result += try_it(x, y)

    return result


def part2():
    grid = [line.strip() for line in sys.stdin]
    height = len(grid)
    width = len(grid[0])

    def try_it(x, y):
        down_slash = False
        up_slash = False
        if (grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S') or\
           (grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M'):
            down_slash = True

        if (grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S') or\
           (grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M'):
            up_slash = True

        if down_slash and up_slash:
            return 1
        return 0

    result = 0
    for y in range(height):
        for x in range(width):
            letter = grid[y][x]
            if letter != 'A' or x == 0 or x == width - 1 or y == 0 or y == height - 1:
                continue

            result += try_it(x, y)

    return result


print(part2())

            
