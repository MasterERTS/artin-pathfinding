from lib.world import World
from lib.node import Node

class AStar():
    
    def __init__(self, start, target, diagonals, World):
        self.start = Node(start, target, -1, None, World, diagonals, True)
        self.target = Node(target, target, 0, None, World, diagonals, True)

        self.open_nodes = [self.start]
        self.closed_nodes = []

        self.reached = False
        self.available_tiles = World.list_available_tiles()

        if (not(self.start.is_accessible())):
            stdout.write ("\033[;1m" + "\033[1;31m" )
            stdout.write('START Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            input("New START Tile --->  ")
        if (not(self.target.is_accessible())):
            stdout.write ("\033[;1m" + "\033[1;31m" )
            stdout.write('TARGET Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            input("New TARGET Tile --->  ")

    def shortest_path(self):
        