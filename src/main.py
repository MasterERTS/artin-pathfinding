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
from lib.bfs import BreadthFirstSearch
from lib.pathfinder import *
from lib.dijkstra import Dijkstra

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


def main():
    args = dict([arg.split('=') for arg in sys.argv[1:]])
    algorithm = args['pathfinding']

    if algorithm == 'a*':
        pass
    elif algorithm == 'dijkstra':
        pass
    elif algorithm == 'dfs':
        pass
    elif algorithm == 'bfs':
        pass
    elif algorithm == 'stw':
        pass
    elif algorithm == 'all':
        pass

if __name__ == "__main__":
    bfs()