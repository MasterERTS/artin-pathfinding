from world import World

class PathFinding():
    def __init__(self, World, start, target, path = None, predecessors = None):
        self.env = World
        self.start = start
        self.target = target

        if (predecessors == None):
            self.predecessors = dict()
        else:
            self.predecessors = predecessors
        
        if (path == None):
            self.path = []
        else:
            self.path = path
            

    def reconstructPath(self):
        self.path = [self.target]
        elem = self.target

        while self.predecessors[elem] is not self.start:
            elem = self.predecessors[elem]
            self.path.append(elem)
        if (len(self.path) > 1):
            self.path.append(self.start)