import numpy as np
print('The basics:....')
a=np.array([20,30,40,50])
b=np.arange(4)
print(b)

c= a-b 
print(c)

print(b**2)

print(10*np.sin(a))

print(a<35)

print('Matrix Multipliaction:.....')

A= np.array([[1,1],[0,1]])
B= np.array([[2,0],[3,4]])

print('Product wise mult')
print( A*B)
print('Matrix mult')
print(A@B)
print(A.dot(B))

