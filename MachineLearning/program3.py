import numpy as np
import statistics as stats
numbers = [1,2,3,4,5,6,6]
n= len(numbers)
print('mean of the entered data :',np.mean(numbers))
print('median of the entered data:', np.median(numbers))
print('Mode of the entered data:', stats.mode(numbers))
print('variance of the entered data',np.var(numbers))
print('variance of the entered data',np.std(numbers))