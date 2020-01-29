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
    main()
