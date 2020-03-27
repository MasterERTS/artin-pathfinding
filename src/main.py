# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : pathfinding algorithms database
@args : algorithm names : ...tbd
'''

import time
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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

# --------------------------------------------- #


def bfs(env, allow_diagonals, display):
    first = env.get_start()
    last = env.get_target()
    pathfinder = BreadthFirstSearch(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def spanningtreewalk(env, allow_diagonals, display):
    first = env.get_start()
    last = env.get_target()
    pathfinder = SpanningTreeWalk(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def dijkstra(env, allow_diagonals, display):
    first = env.get_start()
    last = env.get_target()
    pathfinder = Dijkstra(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def astar(env, allow_diagonals, display):
    first = env.get_start()
    last = env.get_target()
    pathfinder = AStar(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def bidir_astar(env, allow_diagonals, display):
    first = env.get_start()
    last = env.get_target()
    pathfinder = TwoWayAStar(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def dfs(env, allow_diagonals, display):

    first = env.get_start()
    last = env.get_target()
    pathfinder = DepthFirstSearch(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def dataviz(origin_env, allow_diagonals, test_samples, fig_title):
    display = False
    path_astar = []
    path_bidir = []
    path_dfs = []
    path_bfs = []
    path_stw = []
    path_dij = []
    env = origin_env

    for i in range(test_samples):
        env.display()
        startzone = env.list_available_tiles()
        endzone = env.list_available_tiles()
        print(startzone[:10] + endzone[(len(endzone)-10):])
        path_astar.append(astar(env, allow_diagonals, False))
        path_bidir.append(bidir_astar(env, allow_diagonals, False))
        path_dfs.append(dfs(env, allow_diagonals, False))
        path_bfs.append(bfs(env, allow_diagonals, False))
        path_stw.append(spanningtreewalk(env, allow_diagonals, False))
        path_dij.append(dijkstra(env, allow_diagonals, False))
        env = World(origin_env.L, origin_env.H, origin_env.pWalls)
    
    views = PathfindingComparator()
    views.addFigure(3, fig_title)
    views.addPlotToAxs(path_astar, fig_title, 0, "AStar")
    views.addPlotToAxs(path_dij, fig_title, 1, "Dijkstra")
    views.addPlotToAxs(path_bidir, fig_title, 2, "Bidirectional AStar")

    views.addFigure(3, fig_title)
    views.addPlotToAxs(path_dfs, fig_title, 0, "Depth-First Search")
    views.addPlotToAxs(path_bfs, fig_title, 1, "Breadth-First Search")
    views.addPlotToAxs(path_stw, fig_title, 2, "Spanning Tree Walk")

    views.show()


def main():
    algorithm = 'astar'

    env = World(40, 20, 0.2)
    env.display()
    env.display_available_pos()

    allow_diagonals = False
    display = True

    if algorithm == 'astar':
        astar(env, allow_diagonals, display)
    elif algorithm == 'bidir':
        bidir_astar(env, allow_diagonals, display)
    elif algorithm == 'dijkstra':
        dijkstra(env, allow_diagonals, display)
    elif algorithm == 'dfs':
        dfs(env, allow_diagonals, display)
    elif algorithm == 'bfs':
        bfs(env, allow_diagonals, display)
    elif algorithm == 'stw':
        spanningtreewalk(env, allow_diagonals, display)
    elif algorithm == 'all':
        dataviz(env, allow_diagonals)


if __name__ == "__main__":

    env = World(70, 20, 0.25)
    dataviz(env, False, 25, "70x20x0.25 - No Diagonals")

    env = World(20, 70, 0.25)
    dataviz(env, False, 25, "20x70x0.25 - No Diagonals")
