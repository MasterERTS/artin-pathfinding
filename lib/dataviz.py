import matplotlib.pyplot as plt
import numpy as np


class PathfindingComparator():
    def __init__(self):
        self.subplots_n = 0

        self.plots = dict()
        self.figs = dict()
        self.axs = dict()
        self.figs_flags = dict()
        self.axs_available = dict()

    def registerPaths(self, path, pathname):
        self.plots[pathname] = path
        self.subplots_n += 1

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
