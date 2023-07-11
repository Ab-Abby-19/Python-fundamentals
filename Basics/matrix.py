# numpy
# basics of matrix

import numpy as np

a = np.array([1,2,3],)
b = np.array([[12,23,34],[45,56,67]],)

print(a)
print(b)

# dimension
print(a.ndim)
print(b.ndim)

# shape
print(a.shape)
print(b.shape)

# size
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(b.dtype)
print(b.itemsize)
print(b.nbytes)

# get specific element

print(b[1,2])
print(b[1,-1])
print(b[0,:])
print(b[:,1])

# replace element

b[1,2] = 69
print(b)
b[:,2] = 5
print(b)
b[:,2] = [78,89]
print(b)

# startindex:endindex:stepsize

print(b[0,0:3:2])


