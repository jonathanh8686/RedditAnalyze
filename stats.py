import math
import numpy as np
from scipy import stats
import college as clg


colleges = ["ucla", "ucsd", "berkeley", "gatech", "MIT", "brownu", "cmu", "princeton", "harvard", "cornell", "columbia", "dartmouth", "bostonU", "ASU", "caltech", "uiuc",
            "uchicago"]


def ttest(g1, g2):
   a = np.asarray(g1)
   b = np.asarray(g2)

   print(stats.ttest_ind(a, b))
