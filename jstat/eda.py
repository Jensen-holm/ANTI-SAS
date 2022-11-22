import plotille
from jstat.stat import impute_na 



def scatter(x, y, w=15, h=15):
    impute_na(x)
    impute_na(y)
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.set_y_limits(min_=min(y), max_=max(y))
    fig.set_x_limits(min_=min(x), max_=max(x))
    fig.color_mode = "byte"
    fig.scatter(x, y)
    print(fig.show(legend=True))


def histogram(x, w=15, h=15):
    impute_na(x)
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.histogram(x)
    print(fig.show(legend=True))
