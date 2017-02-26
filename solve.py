""" Create and save the output image.
This is simple drawing code that travels between each node in turn,
drawing either a horizontal or vertical line as required.
Line colour is roughly interpolated between blue and red depending
on how far down the path this section is. Dependency on numpy
should be easy to remove at some point. """

import numpy as np
from PIL import Image
import time
from mazes import Maze
from factory import SolverFactory

# Read command line arguments - the python argparse class is convenient here.
import argparse
SF = SolverFactory()
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-m", "--method", nargs='?', const=SF.Default,
                    default=SF.Default, choices=SF.Choices)
PARSER.add_argument("input_file")
PARSER.add_argument("output_file")
ARGS = PARSER.parse_args()

METHOD = ARGS.method   # Never used?

# Load Image
print ("Loading Image")
IMAGE_IN = Image.open(ARGS.input_file)

# Create the maze (and time it)
# - for many mazes this is more time consuming than solving the maze
print ("Creating Maze")
TIME_0 = time.time()
MAZE = Maze(IMAGE_IN)
TIME_1 = time.time()
print ("Node Count:", MAZE.count)
TOTAL = TIME_1-TIME_0
print ("Time elapsed:", TOTAL, "\n")

# Create and run solver
[TITLE, SOLVER] = SF.createsolver(ARGS.method)
print ("Starting Solve:", TITLE)

TIME_0 = time.time()
[RESULT, STATS] = SOLVER(MAZE)
TIME_1 = time.time()

TOTAL = TIME_1-TIME_0

# Print solve stats
print ("Nodes explored: ", STATS[0])
if (STATS[2]):
    print ("Path found, length", STATS[1])
else:
    print ("No Path Found")
print ("Time elapsed: ", TOTAL, "\n")



print ("Saving Image")
MAZE_IMAGE = np.array(IMAGE_IN)
IMAGE_OUT = np.array(MAZE_IMAGE)
IMAGE_OUT[IMAGE_OUT == 1] = 255
OUT = IMAGE_OUT[:, :, np.newaxis]

OUT = np.repeat(OUT, 3, axis=2)

RESULT_PATH = [n.position for n in RESULT]

LENGTH = len(RESULT_PATH)

PIXEL = [0, 0, 0]
for i in range(0, LENGTH - 1):
    a = RESULT_PATH[i]
    b = RESULT_PATH[i+1]

    # Blue - red
    PIXEL[0] = int((i / LENGTH) * 255)
    PIXEL[2] = 255 - PIXEL[0]

    if a[0] == b[0]:
	# Ys equal - horizontal line
        for x in range(min(a[1], b[1]), max(a[1], b[1])):
            OUT[a[0], x, :] = PIXEL
    elif a[1] == b[1]:
	# Xs equal - vertical line
        for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            OUT[y, a[1], :] = PIXEL

IMAGE = Image.fromarray(OUT)
IMAGE.save(ARGS.output_file)
