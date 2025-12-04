
import time

def main():
    part = int(input("Select which part to run for Day 2 (1/2): "))

    if part == 1:
        start = time.perf_counter()
        run_solution(2)
        end = time.perf_counter()
        print(f"part1() took {end - start:.6f} seconds")
    elif part == 2:
        start = time.perf_counter()
        run_solution(12)
        end = time.perf_counter()
        print(f"part2() took {end - start:.6f} seconds")
    else:
        print("dumbass")

def run_solution(num_batteries: int) -> int:
    sum = 0
    with open("input.txt") as file:
        for line in file:
            joltage = calculate_max_joltage(line.strip(), num_batteries)
            sum += joltage

    print(f'total joltage = {sum}')
    return sum

def calculate_max_joltage(bank: str, num_batteries: int) -> int:
    joltage = ""
    print(f'calculating joltage for bank: {bank}')

    for d in range(num_batteries, 0, -1):
        length = len(bank)
        print(bank)
        max = -1
        for i in range(length-(d), -1, -1):
            if int(bank[i]) > int(max):
                max = bank[i]
        new_str_start = bank.find(str(max))+1
        if new_str_start < length:
            bank = bank[bank.find(str(max))+1::]
        joltage += str(max)

    print(f'joltage = {joltage}')
    return int(joltage)

if __name__ == '__main__':
    main()