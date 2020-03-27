# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : dijkstra implementation
'''

from lib.world import World
from lib.node import Node
from sys import stdout


class Dijkstra():

    def __init__(self, start, target, allow_diagonals, World):
        self.start = Node(start, target, 0, None, World,
                          False, allow_diagonals, True)
        self.target = Node(target, target, -1, None, World,
                           False, allow_diagonals, True)

        self.open_nodes = [self.start]
        self.closed_nodes = []

        self.last_node = None

        self.reached = False
        self.available_tiles = World.list_available_tiles()

        while (not(self.start.is_accessible())):
            stdout.write("\033[;1m" + "\033[1;31m")
            stdout.write('START Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            start = int(input("New START Tile --->  "))
            self.start = Node(start, target, 0, None, World,
                              False, allow_diagonals, True)
        while (not(self.target.is_accessible())):
            stdout.write("\033[;1m" + "\033[1;31m")
            stdout.write('TARGET Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            target = int(input("New TARGET Tile --->  "))
            self.target = Node(target, target, 0, None, World,
                               False, allow_diagonals, True)

        self.path = [self.start.tile_pos]

    def shortest_path(self):
        while self.open_nodes:
            self.open_nodes.sort()  # use __lt__ to sort f values
            current_node = self.open_nodes[0]

            if current_node == self.target:
                self.reached = True
                self.last_node = current_node
                self.path = self.reconstruct_path(current_node)
                break

            else:
                self.closed_nodes.append(self.open_nodes.pop(0))

                # get successors (depending on allow_diagonals constructor parameter)
                successors = current_node.successors()

                for s_node in successors:
                    if s_node in self.open_nodes:
                        # pop the node from open_list
                        chosen_one = self.open_nodes.pop(
                            self.open_nodes.index(s_node))

                        if s_node.g_cost < chosen_one.g_cost:
                            self.open_nodes.append(s_node)
                        else:
                            self.open_nodes.append(chosen_one)

                    elif s_node not in self.closed_nodes:
                        self.open_nodes.append(s_node)

        if not(self.reached):
            stdout.write("\033[;1m" + "\033[1;31m")
            stdout.write(
                '========================! NO PATH FOUND !=========================')
            stdout.write("\033[0;0m")
            self.path = self.reconstruct_path(current_node)


    def reconstruct_path(self, node):
        current_node = node
        path = []
        while (current_node != self.start):
            path.append(current_node.tile_pos)
            current_node = current_node.parent

        path.reverse()
        return(path)

    def reconstruct_path_nodes(self, node):
        current_node = node
        path = []
        while (current_node != self.start):
            path.append(current_node)
            current_node = current_node.parent
        path.reverse()
        return(path)

    def path_info(self):
        if self.reached:
            print("\nGoal reached.")

            stdout.write("Using DIJKSTRA, the shortest path between < TILE = " +
                         str(self.start.tile_pos) + " > and < TILE = " +
                         str(self.target.tile_pos) + " > is ")
            stdout.write("\033[1;31m")
            stdout.write("|| " + str(len(self.path)) + " ||\n\n")
            stdout.write("\033[0;0m")

        else:
            print("No path found...\n")
