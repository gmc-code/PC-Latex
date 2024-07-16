from scipy.stats import skewnorm
import numpy as np

np.random.seed(0)
a = -10 # negative shape parameter indicates skewness towards smaller values
data = skewnorm.rvs(a, size=40)
data = np.interp(data, (data.min(), data.max()), (0, 10))
data = (np.rint(data)).astype(int)
data = (','.join(map(str, data)))
print(data)

np.random.seed(0)
a = 10 # negative shape parameter indicates skewness towards smaller values
data = skewnorm.rvs(a, size=40)
data = np.interp(data, (data.min(), data.max()), (0, 10))
data = (np.rint(data)).astype(int)
data = (','.join(map(str, data)))
print(data)