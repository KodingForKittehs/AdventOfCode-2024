# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import, redefined-outer-name
import collections
import functools
from collections import defaultdict
from itertools import combinations, permutations, product
import heapq
import itertools
import importlib
import sys
import time
import re

import igraph
import matplotlib.pyplot as plt
import numpy as np
#import pygame
import shapely
import shapely.plotting
import z3

sys.path.append("./")
import kittehs_funkollection as kf

importlib.reload(kf)
# np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)
np.set_printoptions(edgeitems=10)

inp = "input.txt"
