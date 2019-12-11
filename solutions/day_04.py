from data_parser import *

def main():
    input_range = get_inputs_4()
    password_count = 0
    password_count_2 = 0
    for num in range(input_range[0], input_range[1]):
        digits = str(num)
        always_increasing = True
        same_numbers = False
        same_only_pair = False
        for i in range(0, len(digits)-1):
            if int(digits[i]) > int(digits[i+1]):
                always_increasing = False
                break
            # password 1 condition
            if digits[i] == digits[i+1]:
                same_numbers = True
            # password 2 conditions
            if i == len(digits) - 2 and digits[i] == digits[i+1] and digits[i-1] != digits[i]:
                same_only_pair = True
            if i < len(digits) - 2 and digits[i] == digits[i+1] and digits[i] != digits[i+2] and (i > 0 and digits[i] != digits[i-1] or i == 0):
                same_only_pair = True

        if always_increasing and same_numbers:
            password_count += 1
        if always_increasing and same_only_pair:
            password_count_2 += 1

    print ("Number of possible passwords: %d" % password_count)
    print ("Number of possible passwords_2: %d" % password_count_2)



if __name__ == '__main__':
    main()
