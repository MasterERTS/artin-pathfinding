import sys
import time
import random
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

        self.algorithms = {
            "AStar": self.computePathAStar,
            "Dijkstra": self.computePathDijkstra,
            "BidirAStar": self.computePathBidirAStar,
            "DFS": self.computePathDFS,
            "BFS": self.computePathBFS,
            "SpanningTree": self.computePathSTW
        }

        self.n_algorithms = len(list(self.algorithms.keys()))

        env.display()
        self.__printKeyTiles(env)

    def __printKeyTiles(self, env):
        free_tiles = env.list_available_tiles()
        print(free_tiles[:10] + free_tiles[(len(free_tiles)-10):])

    def setEnv(self, newEnv, diagonals=False):
        self.env = newEnv
        self.start = newEnv.get_start()
        self.target = newEnv.get_target()
        self.diagonals = diagonals
        newEnv.display()
        self.__printKeyTiles(newEnv)

    def computePathBFS(self):
        pathfinder = BreadthFirstSearch(
            self.start, self.target, self.diagonals, self.env)

        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathDFS(self):
        pathfinder = DepthFirstSearch(
            self.start, self.target, self.diagonals, self.env)

        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathSTW(self):
        pathfinder = SpanningTreeWalk(
            self.start, self.target, self.diagonals, self.env)
        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathAStar(self):
        pathfinder = AStar(self.start, self.target, self.diagonals, self.env)

        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathDijkstra(self):
        pathfinder = Dijkstra(self.start, self.target,
                              self.diagonals, self.env)

        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathBidirAStar(self):
        pathfinder = TwoWayAStar(
            self.start, self.target, self.diagonals, self.env)

        init_time = time.clock()

        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.compute_paths()

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def benchmark(self, test_samples, lengths=True, time=False):
        env = self.env
        views = PathfindingComparator()

        if (not(lengths) and not(time)):
            print("Wtf ? Why do you even benchmark shit if you put all benchmark options to False ? Now you get a random one.")
            x = random.random()
            if (x < 0.33):
                lengths = True
            elif (x > 0.33 and x < 0.66):
                time = True
            else:
                lengths = True
                time = True

        if lengths:
            costLists = {
                "AStar": [],
                "Dijkstra": [],
                "BidirAStar": [],
                "DFS": [],
                "BFS": [],
                "SpanningTree": []
            }

        if time:
            timeLists = {
                "AStar": [],
                "Dijkstra": [],
                "BidirAStar": [],
                "DFS": [],
                "BFS": [],
                "SpanningTree": []
            }

        for i in range(test_samples):
            if self.env.L * self.env.H < 100000:
                self.env.display()

            # Computation
            for alg in self.algorithms.keys():
                path, time = self.algorithms[alg]()
                costLists[alg].append(path["Costs"][-1])
                timeLists[alg].append(time)
                print(alg + " successfully computed.")

            self.setEnv(World(env.L, env.H, env.pWalls), self.diagonals)

        if lengths:
            fig_title = "Cost Comparison"
            views.addFigure(3, fig_title)
            i = 0
            for alg in self.algorithms.keys():
                views.addPlotToAxs(costLists[alg], fig_title, i, alg)
                i += 1
                if i > 2:
                    i = 0
                    views.addFigure(3, fig_title)

        if time:
            fig_title = "Computation Time Comparison"
            views.addFigure(3, fig_title)
            i = 0
            for alg in self.algorithms.keys():
                views.addPlotToAxs(timeLists[alg], fig_title, i, alg)
                i += 1
                if i > 2:
                    i = 0
                    views.addFigure(3, fig_title)

        views.show()

    def displayPath(self, path):
        self.env.display_path(path)
