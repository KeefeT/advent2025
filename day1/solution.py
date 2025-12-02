
import time

def main():
    part = int(input("Select which part to run for Day 1 (1/2): "))

    if part == 1:
        start = time.perf_counter()
        part1()
        end = time.perf_counter()
        print(f"part1() took {end - start:.6f} seconds")
    elif part == 2:
        start = time.perf_counter()
        part2()
        end = time.perf_counter()
        print(f"part2() took {end - start:.6f} seconds")
    else:
        print("dumbass")

def part1() -> int:
    zeros = 0
    pos = 50

    with open("input.txt") as file:
        for line in file:
            rotation = int(line[1::])
            if line[0] == 'L':
                rotation = rotation * -1

            pos = pos + rotation

            if pos % 100 == 0:
                zeros += 1

    print(zeros)
    return zeros

def part2() -> int:
    zeros = 0
    pos = 50

    with open("input.txt") as file:
        for line in file:
            rotation = int(line[1::])
            if line[0] == 'L':
                rotation = rotation * -1

            new_pos = pos + rotation

            if rotation > 0:
                #if we're adding to our rolling sum
                # take the difference of new floor - old floor
                # i.e.
                # pos = 95, rotation = 10, new_pos = 105
                # new_pos // 100 = 1, pos // 100 = 0
                # zeros += 1
                zeros += (new_pos // 100) - (pos // 100)
            else:
                # other way around
                # pos = 5, rotation = -10, new_pos = -5
                # (pos - 1) // 100 = 0, (new_pos - 1) // 100 = -1
                # 0 - -1 = 1

                # -1 for this case
                # pos = 0, rotation = -5, new_pos = -5
                # (0 - 1) // 100 = -1, (-5 - 1 // 100) = -1
                # -1 - -1 = 0
                zeros += (pos - 1) // 100 - (new_pos - 1) // 100


            pos = new_pos


    print(zeros)
    return zeros


if __name__ == '__main__':
    main()