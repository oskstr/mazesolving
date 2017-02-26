""" Module docstring placeholder """

from collections import deque

def solve(maze):
    """ Function docstring placeholder """
    start = maze.start
    end = maze.end
    width = maze.width

    queue = deque([start])
    # shape = (maze.height, maze.width) # Unused variable!
    prev = [None] * (maze.width * maze.height)
    visited = [False] * (maze.width * maze.height)

    count = 0

    completed = False

    visited[start.position[0] * width + start.position[1]] = True

    while queue:
        count += 1
        current = queue.pop()

        if current == end:
            completed = True
            break

        for n in current.neighbours:
            if n != None:
                npos = n.position[0] * width + n.position[1]
                if visited[npos] == False:
                    queue.appendleft(n)
                    visited[npos] = True
                    prev[npos] = current

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.position[0] * width + current.position[1]]

    return [path, [count, len(path), completed]]
