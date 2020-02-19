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


def main():
    args = dict([arg.split('=') for arg in sys.argv[1:]])
    algorithm = args['pathfinding']

    if algorithm == 'a*':
        astar()
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