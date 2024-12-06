# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import importlib
import sys
import matplotlib.pyplot as plt
import numpy as np
import shapely
import shapely.plotting
sys.path.append("./")
import kittehs_funkollection as kf
importlib.reload(plt)
importlib.reload(np)
importlib.reload(shapely)
importlib.reload(kf)

cat = kf.eat("input")

