import numpy as np
the_array = np.arange(50).reshape((5, 10))
np.random.shuffle(the_array)
rows = the_array[:2, :]
print(rows)
