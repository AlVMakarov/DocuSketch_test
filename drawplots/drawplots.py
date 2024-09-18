import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np


class draw:
    def __init__(self):
        self.base_path = os.getcwd()
        self.os_sep = os.path.sep
        if not os.path.exists("plots"):
            os.makedirs("plots")


    def draw_plots(self, u1: pd.Series, u2: pd.Series):
        x = np.arange(u1.shape[0])
        # plot creation
        plt.figure(figsize=(16, 12))  # plot size
        plt.plot(x, u1, 'o', color='blue', markerfacecolor='none', label=u1.name, markersize=5)
        plt.plot(x, u2, 'o', color='red', markerfacecolor='none', label=u2.name, markersize=5)
        
        # axis names
        plt.xlabel('name ID', fontsize=18)
        plt.ylabel('deviation value', fontsize=18)

        # add legend
        plt.legend(fontsize=14)

        # save the figure   
        ft = "%Y-%m-%dT%H-%M-%S%z"
        t = datetime.datetime.now().strftime(ft)
        fig_name = f'{self.os_sep}plots{self.os_sep}{u1.name}_{u2.name}_{t}.png'
        
        plt.savefig(self.base_path + fig_name)

