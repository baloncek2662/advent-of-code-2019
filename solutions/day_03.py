import math

from data_parser import *

def main():
    wires = get_inputs_3()
    path_1, path_2 = wires[0], wires[1]
    grid = [["0"]]
    grid = draw_path(grid, path_1, "1")
    grid = draw_path(grid, path_2, "2")

    starting_position = find_starting_position(grid)
    min_distance = 9999999;
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "X":
                position = [j, i]
                distance = get_manhattan_distance(starting_position, position)
                if distance < min_distance:
                    min_distance = distance

    print ("Minimum Manhattan distance: %d" % min_distance)

def draw_path(grid, path, marker):
    position = find_starting_position(grid)
    for instruction in path:
        direction = instruction[0]
        length = int(instruction[1:])
        for i in range(0, length):
            position = change_position(position, direction)
            grid = move(grid, position, direction, marker)
    return grid

def find_starting_position(grid):
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if grid[y][x] == "0":
                return [x, y]


def move(grid, position, direction, marker):
    x, y = position[0], position[1]
    if direction == "R":
        if x == len(grid[0]):
            grid = append_column(grid)
    elif direction == "L":
        if x < 0:
            grid = prepend_column(grid)
            x = x + 1
    elif direction == "D":
        if y == len(grid):
            grid = append_row(grid)
    elif direction == "U":
        if y < 0:
            grid = prepend_row(grid)
            y = y + 1

    if grid[y][x] == "1" and marker != "1":
        grid[y][x] = "X"
    elif grid[y][x] != "0":
        grid[y][x] = marker
    return grid

def change_position(position, direction):
    if position[0] < 0:
        position[0] = 0
    if position[1] < 0:
        position[1] = 0

    if direction == "R":
        position[0] = position[0]+1
    elif direction == "L":
        position[0] = position[0]-1
    elif direction == "U":
        position[1] = position[1]-1
    elif direction == "D":
        position[1] = position[1]+1

    return position

def append_column(grid):
    for row in grid:
        row.append("-")
    return grid

def prepend_column(grid):
    for row in grid:
        row.insert(0, "-")
    return grid

def append_row(grid):
    new_row = []
    for _ in grid[0]:
        new_row.append("-")
    grid.append(new_row)
    return grid

def prepend_row(grid):
    new_row = []
    for _ in grid[0]:
        new_row.append("-")
    grid.insert(0, new_row)
    return grid

def get_manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

if __name__ == '__main__':
    main()
