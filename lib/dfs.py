# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 29/01/2020
@brief : DFS implementation
'''


from lib.world import World
from sys import stdout
from lib.node import Node

class DepthFirstSearch():
    
    def __init__(self, start, target, allow_diagonals, World):
        self.start = Node(start, target, 0, None, World, False, allow_diagonals, True)
        self.target = Node(target, target, 0, None, World, False, allow_diagonals, True)
        self.reached = False
        self.stack = [self.start]
        self.visited = []
        self.path = []

        while (not(self.start.is_accessible())):
            stdout.write ("\033[;1m" + "\033[1;31m" )
            stdout.write('START Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            self.start = input("New START Tile --->  ")
        while (not(self.target.is_accessible())):
            stdout.write ("\033[;1m" + "\033[1;31m" )
            stdout.write('TARGET Tile have no children, choose another one ! ')
            stdout.write("\033[0;0m")
            self.target = input("New TARGET Tile --->  ")
    

    def shortest_path(self):
        while(self.stack):
            current_node = self.stack.pop()

            if current_node not in self.visited:
                self.visited.append(current_node)
                if self.target == current_node:
                    self.reached = True
                    self.path = [elem.tile_pos for elem in self.visited]
                    # self.path = self.reconstruct_path(current_node)
                    break

                successors = current_node.successors()
                for node in successors:
                    if node not in self.visited:
                        self.stack.append(node)
                        node.parent = current_node
                        
        if not(self.reached):
            stdout.write ("\033[;1m" + "\033[1;31m" )
            stdout.write('========================! NO PATH FOUND !=========================')
            stdout.write("\033[0;0m")


    def reconstruct_path(self, node):
        current_node = node
        path = []

        while (current_node != self.start):
            if (current_node in self.visited):
                path.append(current_node.tile_pos)
            current_node = current_node.parent

        path.reverse()
        return(path)

    
    def path_info(self):
        if self.reached:
            print("\nGoal reached.")

            stdout.write("Using DFS, the shortest path between < TILE = " + 
                   str(self.start.tile_pos) + " > and < TILE = " + 
                   str(self.target.tile_pos) + " > is ")   
            stdout.write ("\033[1;31m")
            stdout.write ("|| " + str(len(self.path)) + " ||\n\n")
            stdout.write("\033[0;0m")
                   
        else:
            print("No path found...\n")