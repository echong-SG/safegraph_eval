import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

safegraph_cm = mpl.colors.LinearSegmentedColormap.from_list(
    'WhToBl', ['#ffffff', #0-1 
                '#f7fbff','#f7fbff','#f7fbff','#f7fbff',
                '#deebf7','#deebf7','#deebf7','#deebf7',
                '#c6dbef','#c6dbef','#c6dbef','#c6dbef',
                '#9ecae1','#9ecae1','#9ecae1','#9ecae1',
                '#6baed6','#6baed6','#6baed6','#6baed6',
                '#4292c6','#4292c6','#4292c6','#4292c6',
                '#2171b5','#2171b5','#2171b5','#2171b5',
                '#084594', #29-30
                ], N=30)

def plot_hexbin(df, groundtruth_colname, patterns_colname = "raw_visit_counts", hexbin_gridsize = 30):
    x = df[patterns_colname]
    y = df[groundtruth_colname]
    
    #generate plot parameters based on number of data points
    num_points = min(len(x),len(y)) 
    max_bin_color = num_points / 250
    
    #plotting functions
    plt.hexbin(x,y,gridsize=hexbin_gridsize, cmap=safegraph_cm, vmin=0, vmax=max_bin_color)
    plt.plot(np.arange(max(x)),np.arange(max(x)),color="k",linewidth=3)
    
    #labels
    plt.xlabel(patterns_colname)
    plt.ylabel(groundtruth_colname)
    
    plt.show()