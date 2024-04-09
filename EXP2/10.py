# Calculate the sum of all columns in a 2D NumPy array:
import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sumi=np.sum(my_array,axis=1)
print(sumi)