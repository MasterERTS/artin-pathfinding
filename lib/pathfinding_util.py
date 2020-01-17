from world import World

class PathFinding(object):
    def __init__(self, World, start, target, path, predecessors = None):
        self.env = World
        self.start = start
        self.target = target

        if (predecessors != None):
            self.predecessors = predecessors
        
        self.path = path

    def getHeuristic(self, current_node):
