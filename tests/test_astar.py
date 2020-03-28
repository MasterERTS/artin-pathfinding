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
    print(str(length) + "x" + str(height) + "x" + str(w_percentage))
    return env


def test_admissible_nodiag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = env.get_start()
    last = env.get_target()
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.target.reconstruct_path_nodes()
        for node in node_path:
            assert(node.h_cost <= (node.f_cost))


def test_admissible_diag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = env.get_start()
    last = env.get_target()
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    
    if pathfinder.reached:
        node_path = pathfinder.target.reconstruct_path_nodes()
        for node in node_path:
            assert(node.h_cost <= (node.f_cost))


def test_consistancy_nodiag():
    for i in range(100):
        env = generate_world()
        available_tiles = env.list_available_tiles()
        first = env.get_start()
        last = env.get_target()
        pathfinder = AStar(first, last, False, env)
        pathfinder.shortest_path()
        
        if pathfinder.reached:
            node_path = pathfinder.target.reconstruct_path_nodes()
            for node in node_path:
                if node != pathfinder.start and node != pathfinder.target and node != pathfinder.target.parent:
                    assert(node.parent.h_cost*0.78 <= (abs(node.g_cost - node.parent.g_cost) + math.sqrt(2) + node.h_cost))


def test_consistancy_diag():
    for i in range(100):
        env = generate_world()
        available_tiles = env.list_available_tiles()
        first = env.get_start()
        last = env.get_target()
        pathfinder = AStar(first, last, True, env)
        pathfinder.shortest_path()
        
        if pathfinder.reached:
            node_path = pathfinder.target.reconstruct_path_nodes()
            for node in node_path:
                if node != pathfinder.start and node != pathfinder.target and node != pathfinder.target.parent:
                    assert(node.parent.h_cost*0.88 <= (abs(node.g_cost - node.parent.g_cost) + math.sqrt(2) + node.h_cost))


def test_heuristic_nodiag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = env.get_start()
    last = env.get_target()
    pathfinder = AStar(first, last, False, env)
    pathfinder.shortest_path()
    if pathfinder.reached:
        assert(pathfinder.target.h_cost == 0)


def test_heuristic_diag():
    env = generate_world()
    available_tiles = env.list_available_tiles()
    first = env.get_start()
    last = env.get_target()
    pathfinder = AStar(first, last, True, env)
    pathfinder.shortest_path()
    if pathfinder.reached:
        assert(pathfinder.target.h_cost == 0)