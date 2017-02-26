""" Module docstring placeholder """
from collections import deque

def solve(maze):
    """ Function docstring placeholder """
    start = maze.start
    end = maze.end
    width = maze.width
    stack = deque([start])
    #shape = (maze.height, maze.width) # Unused variable?
    prev = [None] * (maze.width * maze.height)
    visited = [False] * (maze.width * maze.height)
    count = 0

    completed = False
    while stack:
        count += 1
        current = stack.pop()

        if current == end:
            completed = True
            break

        visited[current.position[0] * width + current.position[1]] = True

	#import code
	#code.interact(local=locals())

        for neighbour in current.neighbours:
            if neighbour != None:
                npos = neighbour.position[0] * width + neighbour.position[1]
                if visited[npos] == False:
                    stack.append(neighbour)
                    prev[npos] = current

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.position[0] * width + current.position[1]]

    return [path, [count, len(path), completed]]
