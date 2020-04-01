import sys
import time
import random
import copy
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
from lib.dataviz import Visualizer

class PathFinder():
    def __init__(self, env, autostart=True, diagonals=False, start=None, target=None):
        self.env = env
        self.diagonals = diagonals

        if start != None and target != None:
            self.start = start
            self.target = target    
            self.env.w[self.start] = 2      
        
        elif autostart:
            self.start = env.get_start()
            self.target = env.get_target()
        
        else:
            self.__printKeyTiles(env)
            self.start = int(input("Enter START tile position"))
            self.target = int(input("Enter TARGET tile position"))
            self.env.w[self.start] = 2

        self.envShelve = {}
        self.grids = {}

        self.algorithms = {
            "AStar": self.computePathAStar,
            "Dijkstra": self.computePathDijkstra,
            "BidirAStar": self.computePathBidirAStar,
            "DFS": self.computePathDFS,
            "BFS": self.computePathBFS,
            "SpanningTree": self.computePathSTW
        }

        self.n_algorithms = len(list(self.algorithms.keys()))
        self.__printKeyTiles(env)

        #self.displayEnv()

    def __printKeyTiles(self, env):
        free_tiles = env.list_available_tiles()
        print(free_tiles[:10] + free_tiles[(len(free_tiles)-10):])

    def setEnv(self, newEnv, diagonals=False):
        self.envShelve.remove(self.env)
        self.env = newEnv
        self.env.w[self.start] = 2
        self.start = newEnv.get_start()
        self.target = newEnv.get_target()
        self.diagonals = diagonals
        self.__printKeyTiles(newEnv)

    def __addPathToEnv(self, path):
        env = self.env
        for elem in path:
            env.w[elem] = 2
        return env

    def __addPathToDict(self, path, pathName):
        env = copy.deepcopy(self.env)
        for elem in path:
            env.w[elem] = 2
        self.envShelve[pathName] = env

    def __convertEnvToGrids(self):
        views = Visualizer()
        for elem in self.envShelve.keys():
            self.grids[elem] = views.convertEnvToGrid(self.envShelve[elem])

    def plotPaths(self):
        views = Visualizer()
        self.envShelve["Environment"] = self.env
        self.__convertEnvToGrids()
        views.plotGrids(self.grids)
        views.show()

    def displayEnv(self):
        views = Visualizer()
        grid = views.convertEnvToGrid(self.env)
        views.plotGrid(grid)
        views.show()

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

        self.__addPathToDict(pathfinder.path, "BFS")

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

        self.__addPathToDict(pathfinder.path, "DFS")

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

        self.__addPathToDict(pathfinder.path, "STW")

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

        self.__addPathToDict(pathfinder.path, "A*")

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

        self.__addPathToDict(pathfinder.path, "Dijkstra")

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

        self.__addPathToDict(pathfinder.path, "Bidirectional A*")

        return(pathInfo, final_time)

    def runAll(self, n_times):
        env = self.env

        costLists = {}
        for alg in self.algorithms.keys():
            costLists[alg] = []

        timeLists = {}
        for alg in self.algorithms.keys():
            timeLists[alg] = []

        for i in range(n_times):
            # Computation
            for alg in self.algorithms.keys():
                path, time = self.algorithms[alg]()
                costLists[alg].append(path["Costs"][-1])
                timeLists[alg].append(time)
                print(alg + " successfully computed.")

            self.setEnv(World(env.L, env.H, env.pWalls), self.diagonals)

        self.plotPaths()
        
        return costLists, timeLists

    def benchmark(self, test_samples, lengths=True, time=False):
        env = self.env
        views = Visualizer()

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

        costLists, timeLists = self.runAll(test_samples)

        if lengths:
            fig_title = "Cost Comparison"
            views.addFigure(3, fig_title)
            i = 0
            k = 0
            for alg in self.algorithms.keys():
                views.addPlotToAxs(costLists[alg], fig_title, i, alg)
                i += 1
                k += 1
                if i > 2:
                    i = 0
                    if k < len(list(self.algorithms.keys())):
                        views.addFigure(3, fig_title)

        if time:
            fig_title = "Computation Time Comparison"
            views.addFigure(3, fig_title)
            i = 0
            k = 0
            for alg in self.algorithms.keys():
                views.addPlotToAxs(timeLists[alg], fig_title, i, alg)
                i += 1
                k += 1
                if i > 2:
                    i = 0
                    if k < len(list(self.algorithms.keys())):
                        views.addFigure(3, fig_title)

        views.show()
        