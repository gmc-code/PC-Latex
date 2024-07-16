
# from tkinter import filedialog
import numpy as np

np.random.seed(123)
data1 = np.random.normal(loc=6, scale=1, size=20)
data1 = np.clip(data1, 1,24)
data1 = (np.rint(data1)).astype(int)
data1 = (','.join(map(str, data1)))
print(data1)

data3 = np.random.normal(loc=8, scale=1, size=20)
data3 = np.clip(data3, 1, 24)
data3 = (np.rint(data3)).astype(int)
data3 = (','.join(map(str, data3)))
print(data3)
