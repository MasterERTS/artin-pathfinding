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
    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
    pathfinder = BreadthFirstSearch(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def spanningtreewalk(env, allow_diagonals, display):
    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
    pathfinder = SpanningTreeWalk(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def dijkstra(env, allow_diagonals, display):
    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
    pathfinder = Dijkstra(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def astar(env, allow_diagonals, display):
    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
    pathfinder = AStar(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def bidir_astar(env, allow_diagonals, display):
    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
    pathfinder = TwoWayAStar(first, last, allow_diagonals, env)
    pathfinder.shortest_path()

    if display:
        pathfinder.path_info()
        env.display_path(pathfinder.path)

    return(len(pathfinder.path))


def dfs(env, allow_diagonals, display):

    first = env.list_available_tiles()[0]
    last = env.list_available_tiles()[-1]
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

        first = env.list_available_tiles()[0]
        last = env.list_available_tiles()[-1]

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


def dataviz(env, allow_diagonals):
    display = False
    pass


def main():
    args = dict([arg.split('=') for arg in sys.argv[1:]])
    algorithm = args['pathfinding']

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
    main()
