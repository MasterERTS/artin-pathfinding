from world import World

class Node(object):
    def __init__(self, tile, World):
        self.tile = tile
        self.predecessor = 0

        self.env = World

        self.h_cost = 0
        self.g_cost = 0
        self.f_cost = 0

    def successors(self):
        if self.tile < 0 or self.tile >= self.env.L * self.env.H or self.env.w[self.tile] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 
        else:
            # look in the four adjacent tiles and keep only those with no wall
            return list(filter(lambda x: self.env.w[x] != 1, [self.tile - 1, self.tile + 1, self.tile - self.env.L, self.tile + self.env.L, self.tile - self.env.L - 1, self.tile - self.env.L + 1, self.tile + self.env.L - 1, self.tile + self.env.L + 1]))
        
    def is_accessible(self):
        children = self.successors()
        if children:
            return(True)
        else:
            return(False)


if __name__ == "__main__":
    wrd = World(10, 10, 0)
    nodes = []
    for i in range (wrd.L * wrd.H):
        new_node = Node(i, wrd)
        nodes.append(new_node)
    
    print(nodes[23].successors())
