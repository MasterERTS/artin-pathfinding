'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : Node class for pathfinding graphs in 2D matrix
@todo : slightly move target or start node if not available
'''

from lib.world import World

class Node:
    def __init__(self, tile_pos, target, g_cost, parent, World, is_astar = None, diagonals = None, final_node = None):
        self.tile_pos = tile_pos
        self.g_cost = g_cost
        self.target = target
        self.diagonals = diagonals
        self.final_node = final_node
        self.parent = parent
        self.world = World

        if (is_astar == None):
            self.is_astar = False
            self.h_cost = 0
        else:
            self.is_astar = is_astar
            if is_astar:
                self.h_cost = self.calculate_heuristic()
            else:
                self.h_cost = 0

        self.f_cost = self.g_cost + self.h_cost

        if final_node == None:
            if self.target == self.tile_pos:
                self.final_node = True
            else:
                pass
        else:
            if final_node:
                self.final_node = True
            elif final_node == False:
                self.final_node = False

        if diagonals == None:
            self.diagonals = False
        else:
            self.diagonals = diagonals


    # should slightly correct node pos of start or target if they're not available
    def correct_pos(self):
        pass
    

    def calculate_heuristic(self):
        row_current = int(self.tile_pos / self.world.L)
        col_current = self.tile_pos % self.world.H
        row_target = int(self.target / self.world.L)
        col_target = self.target % self.world.H
        
        if self.diagonals == True:
            return ((row_current - row_target)**2 + (col_current - col_target)**2)**0.5
        else:
            return abs(row_current - row_target) + abs(col_current - col_target)


    def successors(self):
        i = self.tile_pos

        if i < 0 or i >= self.world.L * self.world.H or self.world.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 

        if self.diagonals == True:
            successors = list(filter(lambda x: self.world.w[x] != 1, [i - 1, 
                                                                      i + 1, 
                                                                      i - self.world.L, 
                                                                      i + self.world.L, 
                                                                      i - self.world.L - 1, 
                                                                      i - self.world.L + 1, 
                                                                      i + self.world.L - 1, 
                                                                      i + self.world.L + 1]))
            children_nodes = [Node(elem, self.target, self.g_cost + 1, self, self.world, self.is_astar, self.diagonals, self.final_node) for elem in successors]
            return children_nodes

        else:
            # look in the four adjacent tiles and keep only those with no wall
            successors = list(filter(lambda x: self.world.w[x] != 1, [i - 1, 
                                                                      i + 1, 
                                                                      i - self.world.L, 
                                                                      i + self.world.L]))
            children_nodes = [Node(elem, self.target, self.g_cost + 1, self, self.world, self.is_astar, self.diagonals, self.final_node) for elem in successors]
            return children_nodes
            

    def is_accessible(self, name = None):
        children = self.successors()
        if children:
            return(True)
        else:
            if name != None:
                print(name + " tile is not accessible !")
            else:
                raise("A visited tile is not ACCESSIBLE.")
            return(False)


    def __lt__(self, other):
        # comparison method for sorting priority
        return self.f_cost < other.f_cost


    def __eq__(self, other):
        if (isinstance(other, Node)):
            return self.tile_pos == other.tile_pos
        return False

    
    def __str__(self):
        return 'Node{}'.format(self.tile_pos)

    
    def __repr__(self):
        return 'Node({}, {}, {})'.format(self.tile_pos, self.g_cost, self.parent)