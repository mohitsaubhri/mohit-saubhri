import numpy as np
 
the_array = np.array([[1, 2], [3, 4]])
 
columns_to_append = np.array([[5], [6]])
the_array = np.append(the_array, columns_to_append, 1)
print(the_array)
