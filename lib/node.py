from world import World

class Node():
    def __init__(self, tile, target, g_cost, predecessor, World):
        self.tile = tile
        self.predecessor = predecessor

        self.target = target
        self.env = World

        self.h_cost = self.get_heuristic()
        self.g_cost = g_cost
        self.f_cost = self.h_cost + self.g_cost

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

    def compare_cost(self, other):
        return self.f_cost < other.f_cost

    def get_heuristic(self):
        # Manhattan distance but could use euclidian ?
        row_current = int(self.tile / self.env.L)
        col_current = self.tile % self.env.H
        row_target = int(self.target / self.env.L)
        col_target = self.target % self.env.H
        return abs(row_current - row_target) + abs(col_current - col_target)


if __name__ == "__main__":
    wrd = World(10, 10, 0)
    nodes = []
    for i in range (wrd.L * wrd.H):
        new_node = Node(i, wrd)
        nodes.append(new_node)
    
    print(nodes[23].successors())
