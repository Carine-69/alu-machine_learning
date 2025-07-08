#!/usr/bin/env python3

import numpy as np
poisson = __import('poisson').poisson

np.random.seed(0)
data = np.random.poison(5.,100.tolist())
p1 = poisson(data)
print('Lambtha:', p1.lamtha)

p2 = poisson(lamtha=5)
print('Lamtha:', p2.lamtha)
