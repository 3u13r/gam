#!/usr/bin/env python

import numpy as np


filename = 'zipf.txt'
a = 2 
n = 40000
rng = np.random.default_rng()
s = rng.zipf(a, n)

with open(filename, 'a') as out:
    for var in s:
        out.write(str(var) + '\n')