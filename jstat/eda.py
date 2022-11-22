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
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.x_label = "Theoritical quantities (z-scores)"
    fig.y_label = "Actual values"
    fig.scatter(x, y, label=lab, lc="blue")

    # make the 45 degree line
    q = np.arange(max(x))
    fig.plot(q, q, label="qq line", lc="red")
    print(fig.show(legend=True))
