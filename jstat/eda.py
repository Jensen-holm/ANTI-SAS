import plotille
from jstat.stat import impute_na


def scatter(x, y, w=25, h=15, label=""):
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.set_y_limits(min_=min(y), max_=max(y))
    fig.set_x_limits(min_=min(x), max_=max(x))
    fig.color_mode = "byte"
    fig.scatter(x, y, label=label)
    print(fig.show(legend=True))


def histogram(x, w=25, h=15):
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.histogram(x)
    print(fig.show())
