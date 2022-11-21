import plotille


def scatter(x, y, df):

    x = df[x]
    y = df[y]

    fig = plotille.Figure()
    fig.width = int(max(x))
    fig.height = int(max(y))
    fig.scatter(x, y)
    print(fig.show(legend=True))
