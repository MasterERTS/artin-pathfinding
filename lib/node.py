from world import World

class Node(object):
    def __init__(self, tile):
        self.tile = tile
        self.h_cost = 0
        self.g_cost = 0
        self.f_cost = 0