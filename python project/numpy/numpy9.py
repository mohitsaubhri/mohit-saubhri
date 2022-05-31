import numpy as np

x = np.array([np.nan, 2, 3, 4])
x = x[~np.isnan(x)]
print(x)
