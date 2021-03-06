"""Return solution method.

A simple factory class that imports and returns a relevant
solver when provided a string. Not hugely necessary, but
reduces the code in solve.py, making it easier to read.
"""

class SolverFactory(object):
    """Create an object of a factory class.

    Attributes:
        default (str): Breadth-first method is the default.
        choices (str, optional):
    """
    def __init__(self):
        self.default = "breadthfirst"
        self.choices = ["breadthfirst", "depthfirst",
                        "dijkstra", "astar", "leftturn"]
    @staticmethod
    def createsolver(method):
        """Function docstring placeholder.

        Args:
            method (str): Method of solution e.g. "dijkstra".

        Returns:
            Text explaining which method was choosen
            and function of said method.
        """
        if method == "leftturn":
            import leftturn
            return ["Left turn only", leftturn.solve]
        elif method == "depthfirst":
            import depthfirst
            return ["Depth first search", depthfirst.solve]
        elif method == "dijkstra":
            import dijkstra
            return ["Dijkstra's Algorithm", dijkstra.solve]
        elif method == "astar":
            import astar
            return ["A-star Search", astar.solve]
        else:
            import breadthfirst
            return ["Breadth first search", breadthfirst.solve]
