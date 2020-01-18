'''
author : Erwin Lejeune <erwin.lejeune15@gmail.com>
date : 17/01/2020
'''

from world import World
from node import Node
from pathfinding_util import PathFinding
import sys
from collections import OrderedDict

class AStar(object):
    def __init__(self, World, start, target):
        self.env = World
        self.start = start
        self.target = target

        self.pathfind = PathFinding(self.env, self.start, self.target)

        self.available_tiles = self.env.list_available_tiles()

        if (start not in self.available_tiles) or (target not in self.available_tiles):
            print("Start or Target not available (wall)... Terminating...")
            sys.exit(0)

        self.available_nodes = dict()
        for elem in self.available_tiles:
            new_node = Node(elem, self.env)
            self.available_nodes[elem] = new_node

        self.f_dict = dict()
        self.g_dict = dict()
        self.h_dict = dict()

        for key, value in self.available_nodes.items():
            self.f_dict[key] = value.f_cost
            self.g_dict[key] = value.g_cost
            self.h_dict[key] = value.h_cost
        
        if not(self.available_nodes[start].is_accessible()):
            print("Start Node is not accessible...")
        if not(self.available_nodes[target].is_accessible()):
            print("Target Node is not accessible..") 

        self.reached = False
        self.open_list = [start]
        self.closed_list = []

    def shortest_path(self):
        while(not(self.reached) and self.open_list):
            sorted_f = OrderedDict(sorted(self.f_dict.items(), key = lambda x: x[1]))
            for tile in sorted_f.keys():
                if tile in self.open_list:
                    current_tile = tile
                    self.open_list.remove(tile)
                    self.closed_list.append(current_tile)
                    break
            if self.target in self.closed_list:
                self.reached = True
                break
                
            children = self.available_nodes[current_tile].successors()
            for child_tile in children:
                if child_tile not in self.closed_list:
                    if child_tile in self.open_list:
                        new_g = self.g_dict[current_tile] + 1
                        if self.g_dict[child_tile] > new_g:
                            self.g_dict[child_tile] = new_g

                            self.available_nodes[child_tile].predecessor = current_tile
                            self.pathfind.predecessors[child_tile] = current_tile
                    else:
                        self.g_dict[child_tile] = self.g_dict[current_tile] + 1
                        self.h_dict[child_tile] = self.pathfind.getHeuristic(current_tile)
                        self.available_nodes[child_tile].predecessor = current_tile
                        self.pathfind.predecessors[child_tile] = current_tile
                        self.f_dict[child_tile] = self.g_dict[child_tile] + self.h_dict[child_tile]
                        self.open_list.append(child_tile)
                        
        if self.reached:
            self.pathfind.reconstructPath()
            self.pathfind.path.reverse()

        return(self.reached, self.pathfind.path)


'''
        while (not(reached) and open_list):
        sorted_f = OrderedDict(sorted(f_score.items(), key = lambda x: x[1]))
        for tile in sorted_f.keys():
            if tile in open_list:
                current_tile = tile
                open_list.remove(tile)
                closed_list.append(current_tile)
                break

        if target in closed_list:
            reached = True
            break

        children = World.successors(current_tile)
        for child_tile in children:
            if child_tile not in closed_list:
                if child_tile in open_list:
                    new_g = g_score[current_tile] + 1
                    if g_score[child_tile] > new_g:
                        g_score[child_tile] = new_g
                        predecessor[child_tile] = current_tile
                else:
                    g_score[child_tile] = g_score[current_tile] + 1
                    h_score[child_tile] = heuristic(World, current_tile, target, True)
                    predecessor[child_tile] = current_tile
                    f_score[child_tile] = g_score[child_tile] + h_score[child_tile]
                    open_list.append(child_tile)
                    
        if reached:
            path = get_path(predecessor, start, target)
            path.reverse()

        return(reached, path)
'''

if __name__ == "__main__":
    w = World(10, 10, 0.1)
    w.display()
    astar = AStar(w, 14, 84)
    astar.shortest_path()
    
    w.display_path(astar.pathfind.path)


        