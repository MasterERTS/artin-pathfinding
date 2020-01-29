from lib.world import World

class Node:
    def __init__(self, tile_pos, target, g_cost, parent, World, diagonals = None):
        self.tile_pos = tile_pos
        self.g_cost = g_cost
        self.target = target
        self.diagonals = diagonals
        self.parent = parent
        self.world = World
        self.h_cost = self.calculate_heuristic()
        self.f_cost = self.g_cost + self.h_cost

        if diagonals == None:
            self.diagonals = False
        else:
            self.diagonals = diagonals

    
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
            return successors

        else:
            # look in the four adjacent tiles and keep only those with no wall
            successors = list(filter(lambda x: self.world.w[x] != 1, [i - 1, 
                                                                      i + 1, 
                                                                      i - self.world.L, 
                                                                      i + self.world.L]))
            return successors
            

    def __lt__(self, other):
        # comparison method for sorting priority
        return self.f_cost < other.f_cost

    
    def __str__(self):
        return 'Node{}'.format(self.tile_pos)

    
    def __repr__(self):
        return 'Node({}, {}, {})'.format(self.tile_pos, self.g_cost, self.parent)