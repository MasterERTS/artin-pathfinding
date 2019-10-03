# Example of world building, display, and successor computation for the artificial 
# intelligence path-finding lab
#
# Author: Didier Lime
# Date: 2018-10-03

from random import random
from sys import stdout
import os
import time

class world:
    # initialise the world
    # L is the number of columns
    # H is the number of lines
    # P is the probability of having a wall in a given tile
    def __init__(self, L, H, P):
        self.L = L 
        self.H = H

        # the world is represented by an array with one dimension
        self.w = [0 for i in range(L*H)] # initialise every tile to empty (0)

        # add walls in the first and last columns
        for i in range(H):
            self.w[i*L] = 1
            self.w[i*L+L-1] = 1
        
        # add walls in the first and last lines
        for j in range(L):
            self.w[j] = 1
            self.w[(H-1)*L + j] = 1

        for i in range(H):
            for j in range(L):
                # add a wall in this tile with probability P and provided that it is neither
                # the starting tile nor the goal tile 
                if random() < P and not (i == 1 and j == 1) and not (i == H-2 and j == L-2):
                    self.w[i*L+j] = 1

    # display the world
    def display(self):
        for i in range(self.H):
            for j in range(self.L):
                if self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')

    def display_path(self, path):
        time.sleep(1)
        os.system('clear')
        for i in range(self.H):
            for j in range(self.L):
                if ( i * self.L + j ) in path:
                    stdout.write('*')
                elif self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')

    # compute the successors of tile number i in world w
    def successors(self, i):
        if i < 0 or i >= self.L * self.H or self.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 
        else:
            # look in the four adjacent tiles and keep only those with no wall
            return list(filter(lambda x: self.w[x] != 1, [i - 1, i + 1, i - self.L, i + self.L]))

    # Depth-first search
    # starting from tile number s0, find a path to tile number t
    # return (r, path) where r is true if such a path exists, false otherwise
    # and path contains the path if it exists  
    def dfs(self, s0, t):
        r = False
        path = []
        stack = []
        visited = []

        stack.append(s0)
        path.append(s0)
        visited.append(s0)

        current_tile = s0

        while stack:
            children = self.successors(current_tile)
            for elem in children:
                if elem not in path:
                    if elem not in visited:
                        stack.append(elem)
            
            current_tile = stack.pop()
            visited.append(current_tile)

            if visited[len(visited) - 1] in visited:
                path.append(current_tile)

            else:
                last_tile = path[len(path) - 1]
                current_children = self.successors(current_tile)

                if last_tile in current_children:
                    path.append(current_tile)

            self.display_path(path)
            print(path)
            print(stack)
        
            if t in path:
                r = True
                break
            
        return (r, path)


    def bfs(self, s0, t):
        r = False
        path = []
        stack = []
        visited = []

        stack.append(s0)
        path.append(s0)
        visited.append(s0)

        current_tile = s0

        while stack:
            children = self.successors(current_tile)
            for elem in children:
                if elem not in path:
                    stack.append(elem)
            
            current_tile = stack.pop(0)
            visited.append(current_tile)

            if visited[len(visited) - 1] in visited:
                path.append(current_tile)

            else:
                last_tile = path[len(path) - 1]
                current_children = self.successors(current_tile)

                if last_tile in current_children:
                    path.append(current_tile)

            self.display_path(path)
            print(path)
            print(stack)
        
            if t in path:
                r = True
                break
            
        return (r, path)


    def dijkstra(self, s0, t):

        return 0

    def a_star(self, s0, t):

        return 0


# create a world
w = world(20, 10, 0.2)

# display it 
w.display()

# print the tile numbers of the successors of the starting tile (1, 1)
#print(w.successors(w.L + 1))

path_found, path = w.dfs(21, 164)
path_found_bfs, path_bfs = w.bfs(21, 164)

if path_found:
    print("Goal reached.")
else:
    print("No path found...")

print("DFS path length = " + len(path))
print("BFS path length = " + len(path_bfs))

