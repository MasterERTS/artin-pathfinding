# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : pathfinding algorithms database
@args : algorithm names : ...tbd
'''

from pathfinder import PathFinder
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from lib.world import World


if __name__ == "__main__":
    env = World(70, 20, 0.2)
    pathfinder_api = PathFinder(env)
    pathfinder_api.benchmark(60, True, True)