#!/usr/bin/env python3

import numpy as np
poisson = __import__('poisson').poisson

np.random.seed()
data = np.random.poisson(5.,100).tolist()
p1 = poisson(data)
print('p(9):', p1.pmf(9))

p2 = poisson(data)

print('p(9):', p2.pmf(9))
