# author NoCh4ms
# Code for the 2nd day of AoC 2019


def calculate(memory, noun, verb):
    code_list = get_list()
    code_list[1] = noun
    code_list[2] = verb
    for counter in range(0, len(code_list), 4):
        if code_list[counter] == 1:
            code_list[code_list[counter + 3]] = code_list[code_list[counter + 1]] + code_list[code_list[counter + 2]]
        elif code_list[counter] == 2:
            code_list[code_list[counter + 3]] = code_list[code_list[counter + 1]] * code_list[code_list[counter + 2]]
        else:
            if code_list[counter] == 99:
                return code_list[0]
            print("Invalid opcode " + str(code_list[counter]) + " on position " + str(counter))
            break
    return code_list[0]


def get_list():
    with open("puzzle_input_day2.txt", "r") as f2:
        data = f2.read()
        data_list = data.split(",")
    return list(map(int, data_list))


real_bool = False

for first in range(100):
    for second in range(100):
        if calculate(get_list(), first, second) == 19690720:
            print(first * 100 + second)
            real_bool = True
            break
    if real_bool:
        break

print(calculate(get_list(), 12, 2))
