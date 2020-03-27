import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from lib.bidir_astar import TwoWayAStar
from lib.dijkstra import Dijkstra
from lib.bfs import BreadthFirstSearch
from lib.stw import SpanningTreeWalk
from lib.dfs import DepthFirstSearch
from lib.astar import AStar
from lib.node import Node
from lib.world import World
from lib.dataviz import PathfindingComparator

class PathFinder():
    def __init__(self, env, diagonals=False):
        self.env = env
        self.diagonals = diagonals
        self.start = env.get_start()
        self.target = env.get_target()

        env.display()
        free_tiles = env.list_available_tiles()
        print(free_tiles[:10] + free_tiles[(len(free_tiles)-10):])

    def getPathBFS(self):
        pass

    def getPathDFS(self):
        pathfinder = DepthFirstSearch(self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        return(pathfinder.path)

    def getPathSTW(self):
        pathfinder = SpanningTreeWalk(self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        return(pathfinder.path)

    def getPathAStar(self):
        pass

    def getPathDijkstra(self):
        pass

    def getPathBidirAStar(self):
        pass

    def displayPath(self, path):
        self.env.display_path(path)


