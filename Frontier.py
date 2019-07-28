# Referenced by CMPT 317 assignments


class Frontier(object):
    """
    A base class for frontiers
    """
    def __init__(self):
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

    def is_empty(self):
        return len(self.nodes) == 0


class FrontierFIFO(Frontier):
    """
    First in first out  Queue for BFS algorithm
    """
    def __init__(self):
        Frontier.__init__(self)

    def add(self, aNode):
        self.nodes.append(aNode)

    def remove(self):
        val = self.nodes.pop(0)
        return val


class FrontierLIFO(Frontier):
    """
    Last in first out Stack
    """
    def __init__(self):
        Frontier.__init__(self)

    def add(self,aNode):
        self.nodes.append(aNode)

    def remove(self):
        val = self.nodes.pop()
        return val


class FrontierLIFO_DL(FrontierLIFO):
    """
    Last in first out Stack, the nodes that exceed a limit are discarded
    """
    def __init__(self, limitation):
        FrontierLIFO.__init__(self)
        self.__limitation = limitation
        self._cutoff = False

    def add(self,aNode):
        if aNode.depth <= self.__limitation:
            self.nodes.append(aNode)
        elif not self._cutoff:
            self._cutoff = True

