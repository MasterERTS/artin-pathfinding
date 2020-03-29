import matplotlib.pyplot as plt
import numpy as np


class Visualizer():
    def __init__(self):
        self.subplots_n = 0
        self.env_ploted = 0

        self.plots = dict()
        self.figs = dict()
        self.axs = dict()
        self.figs_flags = dict()
        self.axs_available = dict()

    def registerPaths(self, path, pathname):
        self.plots[pathname] = path
        self.subplots_n += 1

    def convertEnvToGrid(self, env):
        grid = np.zeros((env.H, env.L))
        for i in range(env.H*env.L):
            row_current = int(i / env.L)
            col_current = i % env.L
            grid[row_current][col_current] = env.w[i]

        return grid

    def plotGrids(self, grid_dict):
        # Plot Environment
        plt.rcParams["figure.figsize"] = [8, 8]
        fig = plt.figure("Availability Grid")
        plt.imshow(grid_dict["Environment"])
        grid_dict.pop("Environment")

        # Plot Pathfinders
        plt.rcParams["figure.figsize"] = [12, 12]
        fig = plt.figure("PathFinders")
        graph_per_rows = int(len(list(grid_dict.keys())))
        ind_col = 0
        ind_rows = 0

        for pltKeys in grid_dict.keys():
            if ind_col % graph_per_rows == 0:
                ind_rows += 1
                ind_col = 0
            a = fig.add_subplot(ind_rows, graph_per_rows, ind_col+1)
            grid = grid_dict[pltKeys]
            plt.imshow(grid)
            a.set_title(pltKeys)
            ind_col += 1

    def plotGrid(self, grid):
        plt.rcParams["figure.figsize"] = [12, 12]
        fig = plt.figure("Environment")
        plt.imshow(grid)

    def addFigure(self, nplots, suptitle):
        self.figs[suptitle], self.axs[suptitle] = plt.subplots(
            nplots, figsize=(10, 7), dpi=80, sharex=True, sharey=True)
        self.figs[suptitle].suptitle(suptitle)
        self.axs_available[suptitle] = [elem for elem in range(nplots)]
        self.figs_flags[suptitle] = True

    def addPlotToAxs(self, path, fig_suptitle, axs_n, axs_title='', plotLabel=''):
        if self.figs_flags[fig_suptitle] == True:
            if axs_n in self.axs_available[fig_suptitle]:
                if plotLabel != '':
                    self.axs[fig_suptitle][axs_n].plot(
                        path, c=np.random.rand(3,))
                else:
                    self.axs[fig_suptitle][axs_n].plot(
                        path, c=np.random.rand(3,), label=plotLabel)
                self.axs[fig_suptitle][axs_n].set_title(axs_title)
                self.axs_available[fig_suptitle].remove(axs_n)

            else:
                self.axs[fig_suptitle][axs_n].plot(
                    path, c=np.random.rand(3,), label=plotLabel)
        else:
            print("Error : Trying to add a plot to a Figure that doesn't exist.")

    def show(self):
        plt.show()
