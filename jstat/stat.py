import numpy as np
import pandas as pd
import random


def np_impute(x: np.array, repl = [None]):
    """
    takes in a numpy array and replaces every value that you specify in the
    repl list that is in the array with the mean of the array
    does so in place
    """
    mu: float = np.mean(x)
    for i, j in enumerate(x):
        if j in repl:
            x[i] = mu


def standardize_arr(arr: np.array) -> np.array:
    return (arr - arr.mean()) / arr.std()


if __name__ == "__main__":
    test_arr: np.array = np.array([random.randint(1, 100) for i in range(100)])
    print(standardize_arr(test_arr))
