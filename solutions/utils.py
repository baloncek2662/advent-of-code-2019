def get_inputs_list(day):
    file = open("../inputs/day_%s.txt" % day, "r")
    inputs_list = []
    for val in file.read().split():
        inputs_list.append(int(val))
    file.close()
    return inputs_list

def get_inputs_list_by_comma(day):
    file = open("../inputs/day_%s.txt" % day, "r")
    inputs_list = []
    for val in file.read().split(","):
        inputs_list.append(int(val))
    file.close()
    return inputs_list
