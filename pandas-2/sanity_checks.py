import pandas as pd
import numpy as np


def part_0(x):
    return (
        (isinstance(x, pd.DataFrame)) and
        (x.shape == (0, 0))
    )


def part_1(x):
    return isinstance(x, pd.Series)


def part_2(x):
    return isinstance(x, str)


def part_3(x):
    return np.isscalar(x)


def part_4(x):
    return np.isscalar(x)


def part_5(x):
    return np.isscalar(x)
