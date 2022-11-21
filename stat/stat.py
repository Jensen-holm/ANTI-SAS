import numpy as np
import pandas as pd
import random


def standardize_arr(arr: np.array) -> np.array:
    return (arr - arr.mean()) / arr.std()


if __name__ == "__main__":
    test_arr: np.array = np.array([random.randint(1, 100) for i in range(100)])
    print(standardize_arr(test_arr))
