
import time

def main():
    part = int(input("Select which part to run for Day 2 (1/2): "))

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
    invalid_id_sum = 0

    with open("input.txt") as file: 
        line = file.readline().split(',')
        # print(line)

        for r in line:
            ran = r.split('-')
            low = int(ran[0])
            high = int(ran[1])

            for num in range(low, high + 1):
                if is_invalid(num):
                    invalid_id_sum += num

    print(f'invalid_id_sum = {invalid_id_sum}')

    return invalid_id_sum

def part2() -> int:
    invalid_id_sum = 0

    with open("input.txt") as file: 
        line = file.readline().split(',')
        # print(line)

        for r in line:
            ran = r.split('-')
            low = int(ran[0])
            high = int(ran[1])

            for num in range(low, high + 1):
                if is_more_invalid(num):
                    invalid_id_sum += num

    print(f'invalid_id_sum = {invalid_id_sum}')

    return invalid_id_sum

def is_invalid(num: int) -> bool:
    string = str(num)

    l = len(string)

    if l % 2 == 1:
        return False
    elif string[0:(l//2)] == string[l//2:]:
        return True

    return False

def is_more_invalid(num: int) -> bool:
    string = str(num)
    length = len(string)
    #for every valid substring in string
    for i in range(1,(length//2)+1): # == len substring
        valid = False
        sub = string[:i]
        num_checks = length // i

        if (length % i != 0):
            #cant work
            continue

        # for every check of that substring for 
        for j in range(0,num_checks):
            jsub = string[i*j:(i*j)+i]
            if sub != jsub:
                valid = False
                break
            else:
                valid = True

        if valid == True:
            return True

    return False


if __name__ == '__main__':
    main()