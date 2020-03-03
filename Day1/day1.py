# author NoCh4ms
# Code for the 1st day of AoC 2019


def get_fuel_req(mass):
    return int(mass / 3) - 2


def get_extra_fuel(mass):
    ex_mass = get_fuel_req(mass)
    if ex_mass <= 0:
        return 0
    return ex_mass + get_extra_fuel(ex_mass)


modules = open("puzzle_input.txt")

total_fuel = 0

for module_mass in modules:
    total_fuel += get_extra_fuel(int(module_mass))

print(total_fuel)
