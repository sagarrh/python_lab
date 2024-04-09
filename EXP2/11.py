# Calculate the average, variance, and standard deviation in Python using NumP
import numpy as np

my_array=np.array([1, 2, 3, 4, 5])
average = np.mean(my_array)
variance = np.var(my_array)
sd=np.std(my_array)
print("Average:", average)
print("Variance:", variance)
print("Standard Deviation:", sd)