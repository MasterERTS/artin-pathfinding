# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : pathfinding algorithms database
@args : algorithm names : ...tbd
'''

import numpy as np
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.world import World
from lib.node import Node
from lib.astar import AStar
from lib.dfs import DepthFirstSearch
from lib.stw import SpanningTreeWalk
from lib.bfs import BreadthFirstSearch
from lib.dijkstra import Dijkstra
from lib.bidir_astar import TwoWayAStar
import time

# --------------------------------------------- #

def bfs():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = BreadthFirstSearch(first, last, True, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass


def spanningtreewalk():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = SpanningTreeWalk(first, last, True, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass


def dijkstra():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = Dijkstra(first, last, True, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass


def astar():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass

def bidir_astar():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = TwoWayAStar(first, last, False, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass

def dfs():
    env = World(40, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = DepthFirstSearch(first, last, False, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass


'''
Bidirectional A* is (with this env configuration) 
'''
def comparative_test(allow_diag):
    continuing = True
    while continuing:
        env = World(40, 20, 0)
        env.display()
        env.display_available_pos()

        first = int(input("Start Node --->  "))
        last = int(input("Target Node --->  "))

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

        print("Computation time for BiDir A* = " + str(computation_time_bd_astar) + ' seconds.')
        print("Computation time for A* = " + str(computation_time_astar) + ' seconds.')

        if computation_time_astar > computation_time_bd_astar:
            print("A* is slower than 2-Way A* by " + str(int(computation_time_astar/computation_time_bd_astar*100)) + "%")
        else:
            print("2-Way A* is slower than A* by " + str(int(computation_time_bd_astar/computation_time_astar*100)) + "%")
        break



def main():
    args = dict([arg.split('=') for arg in sys.argv[1:]])
    algorithm = args['pathfinding']

    if algorithm == 'a*':
        astar()
    elif algorithm == 'bidir':
        bidir_astar()
    elif algorithm == 'dijkstra':
        dijkstra()
    elif algorithm == 'dfs':
        dfs()
    elif algorithm == 'bfs':
        bfs()
    elif algorithm == 'stw':
        spanningtreewalk()
    elif algorithm == 'all':
        pass

if __name__ == "__main__":
    bidir_astar()