import sys
import time
import random
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from lib.dataviz import PathfindingComparator
from lib.world import World
from lib.node import Node
from lib.astar import AStar
from lib.dfs import DepthFirstSearch
from lib.stw import SpanningTreeWalk
from lib.bfs import BreadthFirstSearch
from lib.dijkstra import Dijkstra
from lib.bidir_astar import TwoWayAStar

class PathFinder():
    def __init__(self, env, diagonals=False):
        self.env = env
        self.diagonals = diagonals
        self.start = env.get_start()
        self.target = env.get_target()

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
        init_time = time.clock()

        pathfinder = BreadthFirstSearch(
            self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.c

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathDFS(self):
        init_time = time.clock()

        pathfinder = DepthFirstSearch(
            self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.c

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathSTW(self):
        init_time = time.clock()

        pathfinder = SpanningTreeWalk(
            self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.c

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathAStar(self):
        init_time = time.clock()

        pathfinder = AStar(self.start, self.target, self.diagonals, self.env)
        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.c

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathDijkstra(self):
        init_time = time.clock()

        pathfinder = Dijkstra(self.start, self.target,
                              self.diagonals, self.env)
        pathfinder.shortest_path()

        final_time = time.clock() - init_time

        pathfinder.c

        pathInfo = {
            "Path": pathfinder.path,
            "Costs": pathfinder.costs
        }

        return(pathInfo, final_time)

    def computePathBidirAStar(self):
        init_time = time.clock()

        pathfinder = TwoWayAStar(
            self.start, self.target, self.diagonals, self.env)
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
            pathList_astar = []
            pathList_bidir = []
            pathList_dfs = []
            pathList_bfs = []
            pathList_stw = []
            pathList_dij = []

        if time:
            timeList_astar = []
            timeList_bidir = []
            timeList_dfs = []
            timeList_bfs = []
            timeList_stw = []
            timeList_dij = []

        for i in range(test_samples):
            self.env.display()

            # Computation
            path_astar, time_astar = self.computePathAStar()
            path_bidir, time_bidir = self.computePathBidirAStar()
            path_dfs, time_dfs = self.computePathDFS()
            path_bfs, time_bfs = self.computePathBFS()
            path_stw, time_stw = self.computePathSTW()
            path_dij, time_dij = self.computePathDijkstra()

            # Get all Paths for Comparison
            if lengths:
                pathList_astar.append(path_astar["Costs"][-1])
                pathList_bidir.append(path_bidir["Costs"][-1])
                pathList_dfs.append(path_dfs["Costs"][-1])
                pathList_bfs.append(path_bfs["Costs"][-1])
                pathList_stw.append(path_stw["Costs"][-1])
                pathList_dij.append(path_dij["Costs"][-1])

            # Get all Times for Comparison
            if time:
                timeList_astar.append(time_astar)
                timeList_bidir.append(time_bidir)
                timeList_dfs.append(time_dfs)
                timeList_bfs.append(time_bfs)
                timeList_stw.append(time_stw)
                timeList_dij.append(time_dij)

            self.setEnv(World(env.L, env.H, env.pWalls), self.diagonals)

        if lengths:
            fig_title = "Cost Comparison"
            views.addFigure(3, fig_title)
            views.addPlotToAxs(pathList_astar, fig_title, 0, "AStar")
            views.addPlotToAxs(pathList_dij, fig_title, 1, "Dijkstra")
            views.addPlotToAxs(pathList_bidir, fig_title,
                               2, "Bidirectional AStar")

            views.addFigure(3, fig_title)
            views.addPlotToAxs(pathList_dfs, fig_title,
                               0, "Depth-First Search")
            views.addPlotToAxs(pathList_bfs, fig_title,
                               1, "Breadth-First Search")
            views.addPlotToAxs(pathList_stw, fig_title,
                               2, "Spanning Tree Walk")

        if time:
            fig_title = "Computation Time Comparison"
            views.addFigure(3, fig_title)
            views.addPlotToAxs(timeList_astar, fig_title, 0, "AStar")
            views.addPlotToAxs(timeList_dij, fig_title, 1, "Dijkstra")
            views.addPlotToAxs(timeList_bidir, fig_title,
                               2, "Bidirectional AStar")

            views.addFigure(3, fig_title)
            views.addPlotToAxs(timeList_dfs, fig_title,
                               0, "Depth-First Search")
            views.addPlotToAxs(timeList_bfs, fig_title,
                               1, "Breadth-First Search")
            views.addPlotToAxs(timeList_stw, fig_title,
                               2, "Spanning Tree Walk")

        views.show()

    def displayPath(self, path):
        self.env.display_path(path)
