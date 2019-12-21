# Example of world building, display, and successor computation for the artificial 
# intelligence path-finding lab
#
# Author: Didier Lime
# Date: 2018-10-03
# Improved by: Erwin Lejeune, Morgane Talbot
# Date: 2019-10-03

from random import random
from sys import stdout
import os
import time

class World:
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

    # return list of available tiles
    def list_available_tiles(self):
        available_tiles = []
        for i in range(self.L*self.H):
            if self.w[i] == 0:
                available_tiles.append(i)
        return(available_tiles)

    # display the world
    def display(self):
        for i in range(self.H):
            for j in range(self.L):
                if self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')
    
    def display_stepbystep(self, path, rate):
        partial_path = []
        for i in range(len(path)):
            os.system('clear')
            partial_path.append(path[i])
            for i in range(self.H):
                for j in range(self.L):
                    if ( i * self.L + j ) in partial_path:
                        stdout.write("\033[0;32m")
                        stdout.write('¤')
                        stdout.write("\033[0;0m")
                    elif self.w[i * self.L + j] == 0:
                        stdout.write('.')
                    elif self.w[i * self.L + j] == 1:
                        stdout.write ("\033[;1m" + "\033[1;31m" )
                        stdout.write('█')
                        stdout.write("\033[0;0m")

                print('')
            time.sleep(rate)
            

    def display_path(self, path):
        for i in range(self.H):
            for j in range(self.L):
                if ( i * self.L + j ) in path:
                    stdout.write("\033[0;32m")
                    stdout.write('¤')
                    stdout.write("\033[0;0m")
                elif self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write ("\033[;1m" + "\033[1;31m" )
                    stdout.write('█')
                    stdout.write("\033[0;0m")

            print('')

    # compute the successors of tile number i in world w
    def successors(self, i):
        if i < 0 or i >= self.L * self.H or self.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 
        else:
            # look in the four adjacent tiles and keep only those with no wall
            return list(filter(lambda x: self.w[x] != 1, [i - 1, i + 1, i - self.L, i + self.L, i - self.L - 1, i - self.L + 1, i + self.L - 1, i + self.L + 1]))


    def is_accessible(self, i, name):
        children = self.successors(i)
        if children:
            return(True)
        else:
            print(name + " tile is not accessible !")
            return(False)

        

