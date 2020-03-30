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
import numpy as np
import time


class World:
    # initialise the world
    # L is the number of columns
    # H is the number of lines
    # P is the probability of having a wall in a given tile
    def __init__(self, L=20, H=20, P=.1, filename=None):
        self.dim = 2
        self.filename = filename
        if filename == None:
            self.L = L
            self.H = H
            self.pWalls = P

            # the world is represented by an array with one dimension
            # initialise every tile to empty (0)
            self.w = [0 for i in range(L*H)]

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
        else:
            data = np.loadtxt(filename, delimiter=',',
                              dtype='Float64', skiprows=2)

            safety_distance = 1
            drone_altitude = 2

            # minimum and maximum north coordinates
            north_min = np.floor(np.min(data[:, 0] - data[:, 3]))
            north_max = np.ceil(np.max(data[:, 0] + data[:, 3]))

            # minimum and maximum east coordinates
            east_min = np.floor(np.min(data[:, 1] - data[:, 4]))
            east_max = np.ceil(np.max(data[:, 1] + data[:, 4]))

            # given the minimum and maximum coordinates we can
            # calculate the size of the grid.
            north_size = int(np.ceil(north_max - north_min))
            east_size = int(np.ceil(east_max - east_min))
            # Initialize an empty grid
            grid = np.zeros((north_size, east_size))

            # Populate the grid with obstacles
            for i in range(data.shape[0]):
                north, east, alt, d_north, d_east, d_alt = data[i, :]
                if alt + d_alt + safety_distance > drone_altitude:
                    obstacle = [
                        int(np.clip(north - d_north - safety_distance -
                                    north_min, 0, north_size-1)),
                        int(np.clip(north + d_north + safety_distance -
                                    north_min, 0, north_size-1)),
                        int(np.clip(east - d_east - safety_distance -
                                    east_min, 0, east_size-1)),
                        int(np.clip(east + d_east + safety_distance -
                                    east_min, 0, east_size-1)),
                    ]

                    grid[obstacle[0]:obstacle[1]+1,
                         obstacle[2]:obstacle[3]+1] = 1
            np.flip(grid, 0)
            self.grid = np.pad(grid, pad_width=1,
                               mode='constant', constant_values=1)
            self.L = self.grid.shape[1]
            self.H = self.grid.shape[0] 
            self.w = self.grid.flatten()

    # return list of available tiles

    def list_available_tiles(self):
        available_tiles = []
        for i in range(self.L*self.H):
            if self.w[i] == 0:
                available_tiles.append(i)
        return(available_tiles)

    def get_start(self):
        available_tiles = self.list_available_tiles()
        while (len(available_tiles) > 0):
            start_tile = available_tiles.pop(0)
            nigh_tiles = self.neighbours(start_tile)
            if (not(nigh_tiles)):
                continue
            else:
                break
        self.w[start_tile] = 2
        return(start_tile)

    def get_target(self):
        available_tiles = self.list_available_tiles()
        while (len(available_tiles) > 0):
            target_tile = available_tiles.pop()
            nigh_tiles = self.neighbours(target_tile)
            if (not(nigh_tiles)):
                continue
            else:
                break
        return(target_tile)

    def neighbours(self, i):
        if i < 0 or i >= self.L * self.H or self.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return []

        else:
            # look in the four adjacent tiles and keep only those with no wall
            successors = list(filter(lambda x: self.w[x] != 1, [i - 1,
                                                                i + 1,
                                                                i - self.L,
                                                                i + self.L]))
            return successors

        '''if self.diagonals == True:
            successors = list(filter(lambda x: self.w[x] != 1, [i - 1,
                                                                      i + 1,
                                                                      i - self.L,
                                                                      i + self.L,
                                                                      i - self.L - 1,
                                                                      i - self.L + 1,
                                                                      i + self.L - 1,
                                                                      i + self.L + 1]))
            return successors
        '''

    def display_available_pos(self):
        print('\n\n')
        k = 0
        stdout.write("\033[;1m")
        print("List of Available positions : ")
        stdout.write("\033[0;0m")
        print("------------------------------")
        for elem in self.list_available_tiles():
            if elem < 100:
                if (k > self.L):
                    print('\n')
                    k = 0
            if elem > 99:
                if (k > int(self.L * 0.83)):
                    print('\n')
                    k = 0
            stdout.write(str(elem) + ' ')
            k += 1
        stdout.write("\033[0;32m")
        print("\n\nWARNING : Pick available tiles for starting and target positions.\n")
        stdout.write("\033[0;0m")

    # display the world
    def display(self):
        os.system('clear')
        print('')
        carriage = int(self.L/10)
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 1)
        stdout.write("\033[;1m")
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
                    stdout.write("\033[;1m" + "\033[1;31m")
                    stdout.write('█')
                    stdout.write("\033[0;0m")
                elif self.w[i * self.L + j] == 2:
                    stdout.write("\033[0;32m")
                    stdout.write('¤')
                    stdout.write("\033[0;0m")

            print('')

    def display_stepbystep(self, path, rate):
        print('')
        carriage = int(self.L/10)
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 1)
        stdout.write("\033[;1m")
        stdout.write(dashes + "MAP" + dashes + "\n\n")
        stdout.write("\033[0;0m")

        partial_path = []
        for i in range(len(path)):
            os.system('clear')
            partial_path.append(path[i])
            for i in range(self.H):
                for j in range(self.L):
                    if (i * self.L + j) in partial_path:
                        stdout.write("\033[0;32m")
                        stdout.write('¤')
                        stdout.write("\033[0;0m")
                    elif self.w[i * self.L + j] == 0:
                        stdout.write('.')
                    elif self.w[i * self.L + j] == 1:
                        stdout.write("\033[;1m" + "\033[1;31m")
                        stdout.write('█')
                        stdout.write("\033[0;0m")

                print('')
            time.sleep(rate)

    def display_path(self, path):
        print('')
        carriage = int(self.L/10)
        spaces = ' ' * carriage
        dashes = '-' * (carriage + int(self.L/2) - 2)
        stdout.write("\033[;1m")
        stdout.write(dashes + "PATH" + dashes + "\n\n")
        stdout.write("\033[0;0m")

        for i in range(self.H):
            for j in range(self.L):
                if (j == 0):
                    if carriage > 0:
                        stdout.write(spaces)
                if (i * self.L + j) in path:
                    stdout.write("\033[0;32m")
                    stdout.write('¤')
                    stdout.write("\033[0;0m")
                elif self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write("\033[;1m" + "\033[1;31m")
                    stdout.write('█')
                    stdout.write("\033[0;0m")

            print('')
