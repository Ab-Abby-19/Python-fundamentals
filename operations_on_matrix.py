# numpy 
# matrix

import numpy as np
a = np.zeros((7,7))
print(a)

b = np.ones((5,5))
print(b)

c = np.zeros((3,3))
print(c)

c[1,1] = 5
print(c)

b[1:4,1:4] = c
print(b)

a[1:6,1:6] = b
print(a)

# operations on matrix

z = np.array([2,4,6,8])
print(z)
z += 2
print(z)
z -= 2
print(z)
x = z*2
print(x)
y = z.copy()/2
print(y)
z **= 2
print(z)

# multiply 2 matrices

a = np.full([2,3],2)
b = np.full([3,2],3)

print(a)
print(b)

c = np.matmul(a,b)
print(c)

# determinant 

# print(np.linalg.det(a))
# print(np.linalg.det(b))
# print(np.linalg.det(c))

# min,max

d = np.array([[1,2,3],[4,5,6]])
print(np.min(d))
print(np.min(d, axis=0))
print(np.min(d, axis=1))
print(np.max(d))
print(np.max(d, axis=1))
print("sum: " + str(np.sum(d)))



