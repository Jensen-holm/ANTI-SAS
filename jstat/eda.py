import plotille
from jstat.stat import np_impute


def check_data(x, y):
    if len(x) > len(y):
        x = x[:len(y)]
    elif len(y) > len(x):
        y = y[:len(x)]
    np_impute(x)
    np_impute(y)


def scatter(x, y, w=15, h=15, end=" "):
    print(y)
    print(len(x), len(y))
    check_data(x, y)
    print(len(x), len(y))
    fig = plotille.Figure()
    # may want to warn the user to remove outliers first
    fig.width = w
    fig.height = h
    fig.scatter(x, y)
    print(fig.show(legend=True), end=end)


def histogram(x, w=15, h=15, end=" "):
    fig = plotille.Figure()
    fig.width = w
    fig.height = h
    fig.histogram(x)
    print(fig.show(legend=True), end=end)
