# Find the most frequent value in a NumPy array
import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 2, 2, 3, 3])
mostfrquent = np.bincount(my_array).argmax()
print(mostfrquent)