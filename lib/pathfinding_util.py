from world import World

class PathFinding(object):
    def __init__(self, World, start, target, path = None, predecessors = None):
        self.env = World
        self.start = start
        self.target = target

        if (predecessors == None):
            self.predecessors = []
        else:
            self.predecessors = predecessors
        
        if (path == None):
            self.path = []
        else:
            self.path = path

    def getHeuristic(self, current_node):
        # Manhattan distance but could use euclidian ?
        row_current = int(current_node / self.env.L)
        col_current = current_node % self.env.H
        row_target = int(self.target / self.env.L)
        col_target = self.target % self.env.H
        return abs(row_current - row_target) + abs(col_current - col_target)

    def reconstructPath(self):
        self.path = [self.target]
        elem = self.target

        while self.predecessors[elem] is not self.start:
            elem = self.predecessors[elem]
            self.path.append(elem)
        if (len(self.path) > 1):
            self.path.append(self.start)
        return self.path