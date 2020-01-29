# -*- coding: utf-8 -*-

'''
@author: Didier Lime
@date: 2018-10-03
------------------------------
@improved by: Erwin Lejeune
@date: 2019-10-03
@brief : 2D Map building Class
'''

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


    def display_available_pos(self):
        print('\n\n')
        k = 0
        stdout.write ("\033[;1m")
        print("List of Available positions : ")
        stdout.write("\033[0;0m")
        print("------------------------------")
        for elem in self.list_available_tiles():
            if elem < 100:
                if ( k > self.L ):
                    print('\n')
                    k = 0
            if elem > 99:
                if ( k > int(self.L * 0.83) ):
                    print('\n')
                    k = 0
            stdout.write(str(elem) + ' ')
            k += 1
        stdout.write("\033[0;32m")
        print("\n\n/!\ Pick available tiles for starting and target positions.\n")
        stdout.write("\033[0;0m")

    # display the world
    def display(self):
        print('')
        carriage = 30 - self.L
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 1)
        stdout.write ("\033[;1m")
        stdout.write(dashes + "MAP" + dashes + "\n\n")
        stdout.write("\033[0;0m")
        for i in range(self.H):
            for j in range(self.L):
                if (j == 0):
                    if carriage > 0:
                        stdout.write(spaces)
                if self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write ("\033[;1m" + "\033[1;31m" )
                    stdout.write('█')
                    stdout.write("\033[0;0m")

            print('')

    
    def display_stepbystep(self, path, rate):
        print('')
        carriage = 30 - self.L
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 1)
        stdout.write ("\033[;1m")
        stdout.write(dashes + "MAP" + dashes + "\n\n")
        stdout.write("\033[0;0m")

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
        print('')
        carriage = 30 - self.L
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 2)
        stdout.write ("\033[;1m")
        stdout.write(dashes + "PATH" + dashes + "\n\n")
        stdout.write("\033[0;0m")

        for i in range(self.H):
            for j in range(self.L):
                if (j == 0):
                    if carriage > 0:
                        stdout.write(spaces)
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

        

