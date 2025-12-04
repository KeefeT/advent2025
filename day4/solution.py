

import time


def main():
    try: 
        part = int(input("Select which part to run for Day 2 (1/2): "))

        if part == 1:
            start = time.perf_counter()
            get_total_rools()
            end = time.perf_counter()
            print(f"part1() took {end - start:.6f} seconds")
        elif part == 2:
            start = time.perf_counter()
            get_total_rools(True)
            end = time.perf_counter()
            print(f"part2() took {end - start:.6f} seconds")
        else:
            print("dumbass")
    except ValueError:
        print('really?')


def get_total_rools(loop=False) -> int:
    available_rolls_of_paper = 0
    matrix = []

    with open('input.txt') as file:
        for line in file:
            matrix.append(list(line.strip()))

    while True:
        begin = available_rolls_of_paper
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if matrix[y][x] == '@':
                    if is_available(matrix, x, y):
                        available_rolls_of_paper += 1
                        if loop:
                            matrix[y][x] = '.'

        if not loop or available_rolls_of_paper == begin:
            # no more new rolls 
            break

    print(f'available_rolls_of_paper = {available_rolls_of_paper}')

    # for line in matrix:
    #     print(line)

    return available_rolls_of_paper



#
#  [y-1][x-1]--[y-1][x]--[y-1][x+1]
#    [y][x-1]      *       [y][x+1]
#  [y+1][x-1]--[y+1][x]--[y+1][x+1]
#

def is_available(matrix, x, y) -> bool:
    num_adj_rolls = -1

    for i in range(y-1, y+2):
        for j in range(x-1, x+2):

            if not (i < 0 or i > len(matrix)-1 or j < 0 or j > len(matrix[i])-1):
                c = matrix[i][j]
                if c == '@' or c == 'x':
                    num_adj_rolls += 1

    availabe = (num_adj_rolls < 4)

    return availabe

def part2() -> int:
    sum = 0
    return sum


if __name__ == '__main__':
    main()