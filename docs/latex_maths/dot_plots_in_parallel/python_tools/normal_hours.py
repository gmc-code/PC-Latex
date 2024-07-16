
# from tkinter import filedialog
import numpy as np

np.random.seed(123)
data1 = np.random.normal(loc=8, scale=1, size=20)
data1 = np.clip(data1, 1,24)
data1 = (np.rint(data1)).astype(int)

data2 = np.random.normal(loc=18, scale=1, size=20)
data2 = np.clip(data2, 1, 24)
data2 = (np.rint(data2)).astype(int)

data12 = np.concatenate((data1,data2))
data12 = (','.join(map(str, data12)))
print(data12)

data3 = np.random.normal(loc=12, scale=2, size=40)
data3 = np.clip(data3, 1, 24)
data3 = (np.rint(data3)).astype(int)
data3 = (','.join(map(str, data3)))
print(data3)
