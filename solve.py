"""Create and save the output image.

This is simple drawing code that travels between each node in turn,
drawing either a horizontal or vertical line as required.
Line colour is roughly interpolated between blue and red depending
on how far down the path this section is."""

# pylint: disable=C0325

from PIL import Image
import time
from mazes import Maze
from factory import SolverFactory

# Read command line arguments - the python argparse class is convenient here.
import argparse

def solve(factory, method, input_file, output_file):
    """Find a path through a maze.

    Args:
        factory (obj): Object of factory class that provides solver.
        method (str): Method of solution e.g. "dijkstra".
        input_file (file): Image file of maze to solve.
        output_file (str): Name of file for maze with solution if one is found.
    """
    # Load Image
    print("Loading Image")
    image = Image.open(input_file)

    # Create the maze (and time it)
    # - for many mazes this is more time consuming than solving the maze
    print("Creating Maze")
    time_0 = time.time()
    maze = Maze(image)
    time_1 = time.time()
    print("Node Count:", maze.count)
    total = time_1-time_0
    print("Time elapsed:", total, "\n")

    # Create and run solver
    [title, solver] = factory.createsolver(method)
    print("Starting Solve:", title)

    time_0 = time.time()
    [result, stats] = solver(maze)
    time_1 = time.time()

    total = time_1-time_0

    # Print solve stats
    print("Nodes explored: ", stats[0])
    if stats[2]:
        print("Path found, length", stats[1])
    else:
        print("No Path Found")
    print("Time elapsed: ", total, "\n")

    print("Saving Image")
    image = image.convert('RGB')
    impixels = image.load()

    resultpath = [n.position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        pixel = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = pixel
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = pixel

    image.save(output_file)


def main():
    """Parse arguments of solve.py and choose method.

    Breadth-first by default."""

    sf = SolverFactory()
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", nargs='?', const=sf.default,
                        default=sf.default, choices=sf.choices)
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    solve(sf, args.method, args.input_file, args.output_file)

if __name__ == "__main__":
    main()
