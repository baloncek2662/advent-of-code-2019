from utils import *

def main():
    input = get_inputs_list("01")
    total_fuel = 0
    for mass in input:
        total_fuel += calculate_fuel(mass)
    print("Total fuel: %d" % total_fuel)

    total_fuel_fuel = 0
    for mass in input:
        total_fuel_fuel += calculate_fuel_fuel(mass)
    print("Total fuel fuel: %d" % total_fuel_fuel)

def calculate_fuel(mass):
    return int(mass/3 - 2)

def calculate_fuel_fuel(mass):
    required_fuel = calculate_fuel(mass)
    if int(required_fuel) <= 0:
        return 0
    return required_fuel + calculate_fuel_fuel(required_fuel)

if __name__ == '__main__':
    main()
