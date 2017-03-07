# mazesolving
A variety of algorithms to solve mazes from an input image.

![maze image](examples/logo.png)

## About
These are the python files associated with the computerphile video on maze solving. Feel free to use, alter, redistribute the code as you see fit.

## Input
Some example mazes are included in the repository. These were generated either by hand, or using the software [Daedalus](http://www.astrolog.org/labyrnth/daedalus.htm). Once exported I edited the mazes to ensure that the following rules are adhered to:

- Each maze is black and white. White represents paths, black represents walls.
- All mazes are surrounded entirely by black walls.
- One white square exists on the top row of the image, and is the start of the maze.
- One white square exists on the bottom row of the image, and is the end of the maze.

## Examples
Solve the maze perfect2k.png with a depth-first search and output it as perfect2k.solved.png.
### Linux and macOS
```bash
python solve.py -m depthfirst ./examples/perfect2k.png ./examples/perfect2k.solved.png
```
### Windows
```
python solve.py -m depthfirst .\examples\perfect2k.png .\examples\perfect2k.solved.png
```

## Notes
This was just a side project I did for fun over a couple of evenings, I'm sure there are many improvements and extensions you could make if you wanted to. Some things to note:

- The data structures and representations can probably be improved for speed - I only focused a little on efficiency. Mostly I wanted to keep memory usage down, to allow the use of very large mazes.
- The very large mazes use a lot of ram. If you don't have 16Gb at least for the 10k+ x 10k+ mazes, you may run out of memory!
- The current format of the test mazes (short paths, very dense) means that in fact dijkstra and a* usually operate more slowly than simple algorithms. In these cases Dijkstra usually performs the same function as breadth first search, but with more computational overhead. There will be some forms of maze where they are significantly faster.
- Mazes don't need to be square - as long as they are surrounded by black walls. The input image will obviously be square.
- Large areas of white, using my algorithm, will essentially degenerate into an inefficient flood fill - avoid!

- Regarding pull requests and issue tracking. I'm not actively developing this project over the long term. Mostly I want the code to be as it was (at least in general function) at the time of the video. I've accepted some obvious improvements already from people, but if you're looking to add a pull request because you've added to or altered the functionality in a big way, I'd prefer you avoided that.
