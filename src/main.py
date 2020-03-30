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

def computeCostBasedAlg(pathfinder):
    path, time = pathfinder.computePathAStar()
    path1, time1 = pathfinder.computePathBidirAStar()
    path2, time2 = pathfinder.computePathDijkstra()
    path, time = pathfinder.computePathDFS()
    path1, time1 = pathfinder.computePathBFS()
    path2, time2 = pathfinder.computePathSTW()
    
    pathfinder.plotPaths()

def computeAndDisplayAStar(pathfinder):
    path, time = pathfinder.computePathAStar()
    pathfinder.plotPaths()

def computeAndDisplayDijkstra(pathfinder):
    path, time = pathfinder.computePathDijkstra()
    pathfinder.plotPaths()

def computeAndDisplayDFS(pathfinder):
    path, time = pathfinder.computePathDFS()
    pathfinder.displayEnv()
    
def computeAndDisplayBidirAStar(pathfinder):
    path, time = pathfinder.computePathBidirAStar()
    pathfinder.plotPaths()

def showComparisonPlots(pathfinder, test_samples):
    pathfinder_api.benchmark(test_samples, True, True)

if __name__ == "__main__":
    env = World(filename="worlds/colliders.csv")
    _start = 25 * env.L + 100
    _goal = 750* env.L + 370
    pathfinder_api = PathFinder(env)
    pathfinder_api.computePathAStar()
    pathfinder_api.plotPaths()
    #pathfinder_api.displayEnvFigure()
    #showComparisonPlots(pathfinder_api, 20)
    #computeAndDisplayDFS(pathfinder_api)
    #computeAndDisplayAStar(pathfinder_api)
    #computeAndDisplayDijkstra(pathfinder_api)
    #computeAndDisplayBidirAStar(pathfinder_api)