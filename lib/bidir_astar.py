# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : astar implementation
'''


from lib.world import World
from lib.node import Node
from lib.astar import AStar
from sys import stdout

class TwoWayAStar(AStar):
    def __init__(self, start, target, allow_diagonals, World):
        self.first_dir = AStar(start, target, allow_diagonals, World)
        self.second_dir = AStar(target, start, allow_diagonals, World)
