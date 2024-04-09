# Insert a space between characters of all the elements of a given NumPy array:
import numpy as np
ny_array = np.array(["sagar","bharat","harsora"])
new_array = np.array([' '.join(list(x)) for x in ny_array])
print(new_array)