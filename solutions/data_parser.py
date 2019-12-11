def get_inputs_1():
    file = open("../inputs/day_01.txt", "r")
    inputs_list = []
    for val in file.read().split():
        inputs_list.append(int(val))
    file.close()
    return inputs_list

def get_inputs_2():
    file = open("../inputs/day_02.txt", "r")
    inputs_list = []
    for val in file.read().split(","):
        inputs_list.append(int(val))
    file.close()
    return inputs_list

def get_inputs_3():
    file = open("../inputs/day_03.txt", "r")
    wires = []
    for i, line in enumerate(file.read().split()):
        wires.append([])
        for inst in line.split(","):
            wires[i].append(inst)
    return wires

def get_inputs_4():
    file = open("../inputs/day_04.txt", "r")
    range = []
    for i in file.read().split("-"):
        range.append(int(i))
    return range
