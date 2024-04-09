#Check whether a Numpy array contains a specified row
import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
specified_row = [4, 5, 6]
contains_row=np.any(np.all(my_array==specified_row,axis=1))
print("Array contains specified row",contains_row)