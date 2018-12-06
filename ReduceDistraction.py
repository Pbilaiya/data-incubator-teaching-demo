import warnings
import numpy as np

def fxn1():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn1()

np.warnings.filterwarnings('ignore', r'invalid value encountered in less_equal')