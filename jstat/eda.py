import plotille
from jstat.stat import impute_na, standardize_arr
import numpy as np


def scatter(x, y, x_lab="", y_lab="", w=25, h=15, label=""):
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.x_label = x_lab
    fig.y_label = y_lab
    fig.set_y_limits(min_=min(y), max_=max(y))
    fig.set_x_limits(min_=min(x), max_=max(x))
    fig.color_mode = "byte"
    fig.scatter(x, y, label=label)
    print(fig.show())


def histogram(x, x_lab="", y_lab="", w=25, h=15, label=""):
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.x_label = x_lab
    fig.y_label = y_lab
    fig.histogram(x)
    print(fig.show())


def qq_plot(y, lab="", w=25, h=15):
    x = standardize_arr(y)
    x.sort()
    x = [[i/len(x), v] for i, v in enumerate(x)]

    xaxis = [v[1] for v in x]
    yaxis = [v[0] for v in x]

    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.x_label = "Theoritical quantities (z-scores)"
    fig.y_label = "sample values"
    fig.scatter(xaxis, yaxis, label=lab, lc="blue")

    # make the 45 degree line

    

    x = np.arange(min(xaxis), max(xaxis), (max(xaxis) - min(xaxis)) / len(xaxis))
    y = np.arange(min(yaxis), max(yaxis), (max(yaxis) - min(yaxis)) / len(yaxis))

    print(x)
    print(y)

    fig.plot(x, y, label="qq line", lc="red")

    print(fig.show(legend=True))
