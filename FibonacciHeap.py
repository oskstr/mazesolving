""" Module docstring placeholder """
class FibHeap(object):
    """ Class docstring placeholder """
    #### Node Class ####
    class Node(object):
        """ Class docstring placeholder """
        def __init__(self, key, value):
            # key value degree mark / prev next child parent
            self.key = key
            self.value = value
            self.degree = 0
            self.mark = False
            self.parent = self.child = None
            self.previous = self.next = self

        def issingle(self):
            """ Method docstring placeholder """
            return self == self.next

        def insert(self, node):
            """ Method docstring placeholder """
            if node == None:
                return

            self.next.previous = node.previous
            node.previous.next = self.next
            self.next = node
            node.previous = self


        def remove(self):
            """ Method docstring placeholder """
            self.previous.next = self.next
            self.next.previous = self.previous
            self.next = self.previous = self

        def addchild(self, node):
            """ Method docstring placeholder """
            if self.child == None:
                self.child = node
            else:
                self.child.insert(node)
            node.parent = self
            node.mark = False
            self.degree += 1

        def removechild(self, node):
            """ Method docstring placeholder """
            if node.parent != self:
                raise AssertionError("Cannot remove child from ", \
                                     "a node that is not its parent")

            if node.issingle():
                if self.child != node:
                    raise AssertionError("Cannot remove a node ", \
                                         "that is not a child")
                self.child = None
            else:
                if self.child == node:
                    self.child = node.next
                node.remove()

            node.parent = None
            node.mark = False
            self.degree -= 1
    #### End of Node Class ####

    def __init__(self):
        self.minnode = None
        self.count = 0
        self.maxdegree = 0 # Unused variable!

    def isempty(self):
        """ Method docstring placeholder """
        return self.count == 0

    def insert(self, node):
        """ Method docstring placeholder """
        self.count += 1
        self._insertnode(node)
        # return node

    def _insertnode(self, node):
        """ Method docstring placeholder """
        if self.minnode == None:
            self.minnode = node
        else:
            self.minnode.insert(node)
            if node.key < self.minnode.key:
                self.minnode = node
        # return node

    def minimum(self):
        """ Method docstring placeholder """
        if self.minnode == None:
            raise AssertionError("Cannot return minimum of empty heap")
        return self.minnode

    def merge(self, heap):
        """ Method docstring placeholder """
        self.minnode.insert(heap.minnode)
        if self.minnode == None or (heap.minnode != None \
                                    and heap.minnode.key < self.minnode.key):
            self.minnode = heap.minnode
        self.count += heap.count

    def removeminimum(self):
        """ Method docstring placeholder """
        if self.minnode == None:
            raise AssertionError("Cannot remove from an empty heap")

        removed_node = self.minnode
        self.count -= 1

        # 1: Assign all old root children as new roots
        if self.minnode.child != None:
            child = self.minnode.child

            while True:
                child.parent = None
                child = child.next
                if child == self.minnode.child:
                    break

            self.minnode.child = None
            self.minnode.insert(child)

        # 2.1: If we have removed the last key
        if self.minnode.next == self.minnode:
            if self.count != 0:
                raise AssertionError("Heap error: Expected 0 keys," \
                                     "count is " + str(self.count))
            self.minnode = None
            return removed_node

        # 2.2: Merge any roots with the same degree
        logsize = 100
        degreeroots = [None] * logsize
        self.maxdegree = 0
        currentpointer = self.minnode.next

        while True:
            currentdegree = currentpointer.degree
            current = currentpointer
            currentpointer = currentpointer.next
            while degreeroots[currentdegree] != None:
                other = degreeroots[currentdegree]
                # Swap if required
                if current.key > other.key:
                    temp = other
                    other = current
                    current = temp

                other.remove()
                current.addchild(other)
                degreeroots[currentdegree] = None
                currentdegree += 1

            degreeroots[currentdegree] = current
            if currentpointer == self.minnode:
                break

        # 3: Remove current root and find new minnode
        self.minnode = None
        newmaxdegree = 0
        for degree in range(0, logsize):
            if degreeroots[degree] != None:
                degreeroots[degree].next = degreeroots[degree].previous = degreeroots[degree]
                self._insertnode(degreeroots[degree])
                if degree > newmaxdegree:
                    newmaxdegree = degree

        maxdegree = newmaxdegree

        return removed_node


    def decreasekey(self, node, newkey):
        """ Method docstring placeholder """
        if newkey > node.key:
            #import code
            #code.interact(local=locals())
            raise AssertionError("Cannot decrease a key to a greater value")
        elif newkey == node.key:
            return

        node.key = newkey

        parent = node.parent

        if parent == None:
            if newkey < self.minnode.key:
                self.minnode = node
            return
        elif parent.key <= newkey:
            return

        while True:
            parent.removechild(node)
            self._insertnode(node)

            if parent.parent == None:
                break
            elif parent.mark == False:
                parent.mark # Pointless statement?
                break
            else:
                node = parent
                parent = parent.parent
                continue
