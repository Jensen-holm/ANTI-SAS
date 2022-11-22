import plotille


def check_data(x, y):
    if len(x) > len(y):
        x = x[:len(y)]
    elif len(y) > len(x):
        y = y[:len(x)]

    x.fillna(x.mean(), inplace=True)
    y.fillna(y.mean(), inplace=True)


def scatter(x, y, w=15, h=15, end=" "):
    check_data(x, y)
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
