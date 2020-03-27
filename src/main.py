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


'''
Bidirectional A* is (with this env configuration) 
'''


def comparative_test(allow_diag):
    continuing = True
    while continuing:
        env = World(40, 20, 0)
        env.display()
        env.display_available_pos()

        first = env.get_start()
        last = env.get_target()

        zero_time_bd_astar = time.clock()
        pathfinder = TwoWayAStar(first, last, allow_diag, env)
        pathfinder.shortest_path()
        computation_time_bd_astar = time.clock() - zero_time_bd_astar

        if(not(pathfinder.reached)):
            continuing = False
            continue

        pathfinder.path_info()
        env.display_path(pathfinder.path)

        time.sleep(2)

        zero_time_astar = time.clock()
        pathfinder_bis = AStar(first, last, allow_diag, env)
        pathfinder_bis.shortest_path()

        computation_time_astar = time.clock() - zero_time_astar
        pathfinder_bis.path_info()

        env.display_path(pathfinder_bis.path)

        time.sleep(2)

        print("Computation time for BiDir A* = " +
              str(computation_time_bd_astar) + ' seconds.')
        print("Computation time for A* = " +
              str(computation_time_astar) + ' seconds.')

        if computation_time_astar > computation_time_bd_astar:
            print("A* is slower than 2-Way A* by " +
                  str(int(computation_time_astar/computation_time_bd_astar*100)) + "%")
        else:
            print("2-Way A* is slower than A* by " +
                  str(int(computation_time_bd_astar/computation_time_astar*100)) + "%")
        break


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

    fig, axs = plt.subplots(6, sharex = True, sharey = True)
    fig.suptitle(fig_title)
    axs[0].plot(path_astar, c=np.random.rand(3,))
    axs[0].set_title("AStar Paths")
    axs[1].plot(path_bidir, c=np.random.rand(3,))
    axs[1].set_title("Bidirectional AStar Paths")
    axs[2].plot(path_dij, c=np.random.rand(3,))
    axs[2].set_title("Dijkstra Paths")
    axs[3].plot(path_bfs, c=np.random.rand(3,))
    axs[3].set_title("Breadth-First Search Paths")
    axs[4].plot(path_stw, c=np.random.rand(3,))
    axs[4].set_title("Spanning Tree Walk Paths")
    axs[5].plot(path_dfs, c=np.random.rand(3,))
    axs[5].set_title("Depth-First Search Paths")


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

    env = World(40, 40, 0.2)
    dataviz(env, False, 25, "40x40x0.2 - No Diagonals")

    env2 = World(50, 20, 0.2)
    dataviz(env2, False, 25, "50x20x0.2 - No Diagonals")

    env = World(40, 40, 0.2)
    dataviz(env, False, 25, "40x40x0.5 - No Diagonals")

    env2 = World(50, 20, 0.2)
    dataviz(env2, False, 25, "50x20x0.5 - NoDiagonals")

    env = World(40, 40, 0.2)
    dataviz(env, True, 25, "40x40x0.2 - Diagonals")

    env2 = World(50, 20, 0.2)
    dataviz(env2, True, 25, "50x20x0.2 - Diagonals")

    env = World(40, 40, 0.2)
    dataviz(env, True, 25, "40x40x0.5 - Diagonals")

    env2 = World(50, 20, 0.2)
    dataviz(env2, True, 25, "50x20x0.5 - Diagonals")

    plt.show()