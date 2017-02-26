""" Method docstring placeholder """
from collections import deque

def solve(maze):
    """ Function docstring placeholder """
    path = deque([maze.start])
    current = maze.start.neighbours[2]
    if current == None:
        return path

    heading = 2 # South
    turn = 1 # Turning left, -1 for right

    startpos = maze.start.position
    endpos = maze.end.position
    # N E S W - just a helpful reminder
    # 0 1 2 3
    count = 1
    completed = False

    while True:
        path.append(current)
        count += 1
        position = current.position
        if position == startpos or position == endpos:
            if position == endpos:
                completed = True
                break
        neighbour = current.neighbours
        if neighbour[(heading - turn) % 4] != None:
            heading = (heading - turn) % 4
            current = neighbour[heading]
            continue
        if neighbour[heading] != None:
            current = neighbour[heading]
            continue
        if neighbour[(heading + turn) % 4] != None:
            heading = (heading + turn) % 4
            current = neighbour[heading]
            continue
        if neighbour[(heading + 2) % 4] != None:
            heading = (heading + 2) % 4
            current = neighbour[heading]
            continue

        completed = False
        break

    return [path, [count, len(path), completed]]
