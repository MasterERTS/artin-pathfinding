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

def computeAndDisplayAStar(pathfinder):
    path, time = pathfinder.computePathAStar()
    pathfinder.displayPath(path["Path"])
    print(path["Costs"])
    print("\n Total Cost = " + str(path["Costs"][-1]))

def computeAndDisplayDijkstra(pathfinder):
    path, time = pathfinder.computePathDijkstra()
    pathfinder.displayPath(path["Path"])
    print(path["Costs"])
    print("\n Total Cost = " + str(path["Costs"][-1]))

def computeAndDisplayDFS(pathfinder):
    path, time = pathfinder.computePathDFS()
    pathfinder.displayPath(path["Path"])
    print(path["Costs"])
    print("\n Total Cost = " + str(path["Costs"][-1]))

def computeAndDisplayBidirAStar(pathfinder):
    path, time = pathfinder.computePathBidirAStar()
    pathfinder.displayPath(path["Path"])
    print('')
    print(path["Costs"])
    print("\n Total Cost = " + str(path["Costs"][-1]))

def showComparisonPlots(pathfinder, test_samples):
    pathfinder_api.benchmark(test_samples, True, True)

if __name__ == "__main__":
    env = World(20, 20, 0.25)
    pathfinder_api = PathFinder(env, True)
    showComparisonPlots(pathfinder_api, 10)
    #computeAndDisplayDFS(pathfinder_api)
    #computeAndDisplayAStar(pathfinder_api)
    #computeAndDisplayDijkstra(pathfinder_api)
    #computeAndDisplayBidirAStar(pathfinder_api)