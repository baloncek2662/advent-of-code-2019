from utils import *

def main():
    values_list = get_inputs_list_by_comma("02")

    executable = values_list.copy()
    executable[1] = 12
    executable[2] = 2
    execute_program(executable)
    print("Final value at position 0: %d" % executable[0])

    solution = find_noun_verb(values_list)
    print("Noun: %d\tVerb: %d\tSolution: %d" % (solution["noun"], solution["verb"], 100*solution["noun"]+solution["verb"]))


def execute_program(values_list):
    position = 0
    try:
        while position < len(values_list):
            operation = values_list[position]
            if operation == 99:
                break;
            pos1, pos2, store =  values_list[position + 1], values_list[position + 2], values_list[position + 3]
            op1, op2 = values_list[pos1], values_list[pos2]
            if operation == 1:
                values_list[store] = op1 + op2
            elif operation == 2:
                values_list[store] = op1 * op2

            position += 4
    except:
        return [0]
    return values_list

def find_noun_verb(values_list):
    noun, verb = -1, -1
    for n in range(0, 100):
        for v in range(0, 100):
            temp = values_list.copy()
            temp[1], temp[2] = n, v
            if execute_program(temp)[0] == 19690720:
                noun, verb = n, v
                break
    return {"noun" : noun, "verb" : verb}


if __name__ == '__main__':
    main()
