# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : Node object tests
'''

import numpy as np
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.world import World
from lib.node import Node
from lib.pathfinder import *


def test_uniqueness():
    env = World(10, 10, 0.2)
    free_tiles = env.list_available_tiles()
    nodes = [Node(i, 84, 0, None, env) for i in free_tiles]

    # list of positions
    pos = []
    for elem in nodes:
        pos.append(elem.tile_pos)

    # check uniqueness
    seen = set()
    uniqueness = not any(k in seen or seen.add(k) for k in pos)

    assert(uniqueness == True)

def test_outofbounds():
    env = World(10, 10, 0.2)
    free_tiles = env.list_available_tiles()
    new_node = [Node(i, 84, 0, None, env) for i in free_tiles]

    for elem in new_node:
        assert(elem.tile_pos >= 0 and elem.tile_pos <= (env.L*env.H))

def test_availability():
    env = World(10, 10, 0.2)
    free_tiles = env.list_available_tiles()

    new_node = [Node(i, 84, 0, None, env) for i in free_tiles]

    for elem in new_node:
        assert(env.w[elem.tile_pos] != 1)
