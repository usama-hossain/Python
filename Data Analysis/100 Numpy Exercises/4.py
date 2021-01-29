# 4. How to find the memory size of any array 

import numpy as np 

Z = np.zeros(10)

print("%d bytes" % (Z.size * Z.itemsize))