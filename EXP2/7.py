#  Compute mathematical operations on Array, Add & Multiply two matrices
import numpy as np

array1 = np.array([[1,2],[3,4]])
array2=np.array([[5,6],[7,8]])

addition = np.add(array1,array2)
print("Addition result:")
print(addition)
multi=np.dot(array1,array2)
print("multiplication is ")
print(multi)
