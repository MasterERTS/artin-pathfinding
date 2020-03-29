'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : Node class for pathfinding graphs in 2D matrix
@todo : slightly move target or start node if not available
'''

from lib.world import World
from math import sqrt

class Node:
    def __init__(self, tile_pos, target, g_cost, parent, World, is_astar=False, diagonals=False):
        self.tile_pos = tile_pos
        self.g_cost = g_cost
        self.target = target
        self.diagonals = diagonals
        self.parent = parent
        self.world = World
        self.diagonals = diagonals

        if is_astar:
            self.is_astar = True
            self.h_cost = self.calculate_heuristic()
        else:
            self.is_astar = False
            self.h_cost = 0
        self.f_cost = self.g_cost + self.h_cost

    # should slightly correct node pos of start or target if they're not available
    def correct_pos(self):
        pass

    def calculate_heuristic(self):
        row_current = int(self.tile_pos / self.world.L)
        col_current = self.tile_pos % self.world.L
        row_target = int(self.target / self.world.L)
        col_target = self.target % self.world.L

        dy = abs(row_current - row_target)
        dx = abs(col_current - col_target)

        if self.diagonals == False:
            return (1 * (dx + dy))
        else:
            dy = abs(row_current - row_target)
            dx = abs(col_current - col_target)
            return(1 * max(dx, dy) + (sqrt(2) - 1) * min(dx, dy))

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

            children_nodes = []
            for elem in successors:
                if elem == (i-1) or elem == (i+1) or elem == (i - self.world.L) or elem == (i + self.world.L):
                    children_nodes.append(Node(elem, self.target, self.g_cost + 1, self, self.world,
                                   self.is_astar, self.diagonals))
                else:
                    children_nodes.append(Node(elem, self.target, self.g_cost + sqrt(2), self, self.world,
                                   self.is_astar, self.diagonals))
            return children_nodes

        else:
            # look in the four adjacent tiles and keep only those with no wall
            successors = list(filter(lambda x: self.world.w[x] != 1, [i - 1,
                                                                      i + 1,
                                                                      i - self.world.L,
                                                                      i + self.world.L]))
            children_nodes = [Node(elem, self.target, self.g_cost + 1, self, self.world,
                                   self.is_astar, self.diagonals) for elem in successors]
            return children_nodes

    def is_accessible(self, name=None):
        children = self.successors()
        if children:
            return(True)
        else:
            if name != None:
                print(name + " tile is not accessible !")
            else:
                print("A visited tile is not ACCESSIBLE.")
            return(False)

    def reconstruct_path(self):
        current_node = self
        path = []
        costs = []
        while (current_node.parent != None):
            path.append(current_node.tile_pos)
            costs.append(current_node.g_cost)
            current_node = current_node.parent

        path.append(current_node.tile_pos)
        costs.append(current_node.g_cost)
        path.reverse()
        costs.reverse()
        return(path, costs)

    def reconstruct_path_nodes(self):
        current_node = self
        path = []
        while (current_node.parent != None):
            path.append(current_node)
            current_node = current_node.parent

        path.append(current_node)

        path.reverse()
        return(path)

    def reconstruct_costs(self):
        current_node = self
        costs = []
        while (current_node.parent != None):
            costs.append(current_node.g_cost)
            current_node = current_node.parent

        costs.append(current_node.g_cost)

        costs.reverse()
        return(costs)

    def __lt__(self, other):
        # comparison method for sorting priority
        if self.f_cost == other.f_cost:
            self.f_cost *= 1.001
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        if (isinstance(other, Node)):
            return self.tile_pos == other.tile_pos
        return False

    def __str__(self):
        return 'Node{}'.format(self.tile_pos)

    def __repr__(self):
        return 'Node({}, {}, {})'.format(self.tile_pos, self.g_cost, self.parent)
