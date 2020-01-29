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
from lib.pathfinder import *

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
    env = World(20, 20, .2)
    env.display()
    env.display_available_pos()

    first = int(input("Start Node --->  "))
    last = int(input("Target Node --->  "))
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    pathfinder.path_info()

    env.display_path(pathfinder.path)

    while(1):
        pass

