# load file data

import numpy as np

filedata = np.genfromtxt("data.txt", delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

print(filedata>20)
print(filedata[filedata > 20])

print(np.any(filedata > 15, axis=0))
print(np.any(filedata > 15, axis=1))

k = filedata[np.any(filedata > 15, axis=1)]
print(k)
