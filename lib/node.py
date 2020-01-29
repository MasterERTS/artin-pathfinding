from lib.world import World

class Node:
    def __init__(self, tile_pos, g_cost, parent):
        self.tile_pos = tile_pos
        self.g_cost = g_cost
        self.h_cost = self.calculate_heuristic()
        self.f_cost = self.g_cost + self.h_cost