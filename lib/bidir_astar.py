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

        self.reached = False
        self.first_dir_reached = False
        self.second_dir_reached = False

        self.path = self.first_dir.path
        self.costs = self.first_dir.costs

    def shortest_path(self):
        while self.first_dir.open_nodes and self.second_dir.open_nodes:
            self.first_dir.open_nodes.sort()
            self.second_dir.open_nodes.sort()
            first_dir_node = self.first_dir.open_nodes[0]
            second_dir_node = self.second_dir.open_nodes[0]

            if first_dir_node.tile_pos == second_dir_node.tile_pos:
                self.reached = True
                self.f_meeting = first_dir_node
                self.s_meeting = second_dir_node
                break

            elif (first_dir_node == self.first_dir.target):
                self.first_dir_reached = True
                self.first_dir.target = first_dir_node
                break

            elif(second_dir_node == self.second_dir.target):
                self.second_dir_reached = True
                self.second_dir.target = second_dir_node
                break

            else:
                self.first_dir.closed_nodes.append(
                    self.first_dir.open_nodes.pop(0))
                self.second_dir.closed_nodes.append(
                    self.second_dir.open_nodes.pop(0))

                first_successors = first_dir_node.successors()
                second_successors = second_dir_node.successors()

                for first_s_node in first_successors:
                    if first_s_node in self.first_dir.open_nodes:
                        first_chosen_one = self.first_dir.open_nodes.pop(
                            self.first_dir.open_nodes.index(first_s_node))

                        if first_s_node.g_cost < first_chosen_one.g_cost:
                            self.first_dir.open_nodes.append(first_s_node)
                        else:
                            self.first_dir.open_nodes.append(first_chosen_one)

                    elif first_s_node not in self.first_dir.closed_nodes:
                        self.first_dir.open_nodes.append(first_s_node)

                for second_s_node in second_successors:
                    if second_s_node in self.second_dir.open_nodes:
                        second_chosen_one = self.second_dir.open_nodes.pop(
                            self.second_dir.open_nodes.index(second_s_node))

                        if second_s_node.g_cost < second_chosen_one.g_cost:
                            self.second_dir.open_nodes.append(second_s_node)
                        else:
                            self.second_dir.open_nodes.append(
                                second_chosen_one)

                    elif second_s_node not in self.second_dir.closed_nodes:
                        self.second_dir.open_nodes.append(second_s_node)

        if not(self.reached):
            stdout.write("\033[;1m" + "\033[1;31m")
            stdout.write(
                '========================! NO PATH FOUND !=========================')
            stdout.write("\033[0;0m")

    def compute_paths(self):
        if self.reached:
            self.path, self.costs = self.reconstruct_path(
                self.f_meeting, self.s_meeting)

        elif self.first_dir_reached:
            self.path, self.costs = self.first_dir.target.reconstruct_path()
        
        elif self.second_dir_reached:
            self.path, self.costs = self.second_dir.target.reconstruct_path()

    def reconstruct_path(self, f_node, s_node):
        # Might be an issue
        first_path, first_costs = f_node.reconstruct_path()
        second_path, second_costs = s_node.reconstruct_path()
        first_path.reverse()
        second_costs.pop(0)
        for i in range(len(second_costs)):
            second_costs[i] += first_costs[-1]
        path = first_path + second_path
        costs = first_costs + second_costs
        return(path, costs)

    def path_info(self):
        if self.reached:
            print("\nGoal reached.")

            stdout.write("Using Bidirectional A*, the shortest path between < TILE = " +
                         str(self.first_dir.start.tile_pos) + " > and < TILE = " +
                         str(self.first_dir.target.tile_pos) + " > is ")
            stdout.write("\033[1;31m")
            stdout.write("|| " + str(len(self.path)) + " ||\n\n")
            stdout.write("\033[0;0m")

        else:
            print("\n\nNo path info...\n")
