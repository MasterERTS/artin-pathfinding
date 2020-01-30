# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : AStar object tests
'''

import numpy as np
import sys
import random
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.world import World
from lib.node import Node
from lib.astar import AStar
import math


def generate_world():
    length = random.randint(10, 50)
    height = random.randint(10, 50)
    w_percentage = random.random() / 4
    env = World(length, height, w_percentage)

    return env


def test_admissible_nodiag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.reconstruct_path_nodes(pathfinder.last_node)
        node_path.reverse()
        for node in node_path:
            assert(node.h_cost <= (node.f_cost))


def test_admissible_diag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.reconstruct_path_nodes(pathfinder.last_node)
        node_path.reverse()
        for node in node_path:
            assert(node.h_cost <= (node.f_cost))


def test_consistancy_nodiag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.reconstruct_path_nodes(pathfinder.last_node)
        for node in node_path:
            if node != pathfinder.start:
                assert(node.parent.h_cost <= (abs(node.f_cost - node.parent.f_cost) + 1 + node.h_cost))


def test_consistancy_diag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.reconstruct_path_nodes(pathfinder.last_node)
        for node in node_path:
            if node != pathfinder.start:
                assert(node.parent.h_cost <= (abs(node.f_cost - node.parent.f_cost) + math.sqrt(2) + node.h_cost))


def test_heuristic_nodiag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    
    assert(pathfinder.last_node.h_cost == 0)


def test_heuristic_diag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = random.choice(available_tiles)
    last = random.choice(available_tiles)
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    
    assert(pathfinder.last_node.h_cost == 0)