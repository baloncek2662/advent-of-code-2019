import math
import sys

from data_parser import *

def old_main():
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

def main():
    paths = get_inputs_3()
    points_wire_1 = get_wire_points(paths[0])
    points_wire_2 = get_wire_points(paths[1])

    intersections = points_wire_1.intersection(points_wire_2)
    closest_point = get_closest_point(intersections)
    min_distance = get_manhattan_distance(closest_point, [0, 0])
    print ("Minimum Manhattan distance: %d" % min_distance)

    closest_intersection = get_closest_intersection(paths[0], paths[1], intersections)
    print ("Closest intersection: %d" % closest_intersection)

def get_wire_points(instructions):
    points = set()
    position = [0,0]
    for instruction in instructions:
        direction = instruction[0]
        length = int(instruction[1:])
        while length > 0:
            position = move_position(position, direction)
            points.add((position[0], position[1]))
            length -= 1
    return points

def move_position(position, direction):
    if direction == "R":
        position[0] = position[0]+1
    elif direction == "L":
        position[0] = position[0]-1
    elif direction == "U":
        position[1] = position[1]-1
    elif direction == "D":
        position[1] = position[1]+1
    return position

def get_closest_point(intersections):
    center = [0,0]
    min_distance = sys.maxsize
    closest_point = sys.maxsize
    for p in intersections:
        dist = get_manhattan_distance(p, center)
        if dist < min_distance:
            min_distance = dist
            closest_point = p
    return closest_point

def get_closest_intersection(path_1, path_2, intersections):
    closest_distance = sys.maxsize
    for intersection in intersections:
        dist_1 = steps_to_coordinates(path_1, intersection)
        dist_2 = steps_to_coordinates(path_2, intersection)
        dist = dist_1 + dist_2
        if dist < closest_distance:
            closest_distance = dist
    return closest_distance

def steps_to_coordinates(instructions, coordinates):
    position = [0,0]
    steps = 0
    for instruction in instructions:
        direction = instruction[0]
        length = int(instruction[1:])
        while length > 0:
            position = move_position(position, direction)
            length -= 1
            steps += 1
            if tuple(position) == coordinates:
                return steps
    return -1


if __name__ == '__main__':
    #old_main()
    main()
