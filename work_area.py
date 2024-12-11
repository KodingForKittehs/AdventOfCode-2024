# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import functools
from collections import defaultdict
from itertools import combinations, permutations, product
import importlib
import sys
import igraph
import matplotlib.pyplot as plt
import numpy as np
import shapely
import shapely.plotting
sys.path.append("./")
import kittehs_funkollection as kf
importlib.reload(kf)
#np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)
np.set_printoptions(edgeitems=10)



line = kf.file_as_line("input")
