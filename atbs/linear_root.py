# Date: 23/12/19
# This program will find the roots of a linear equation
import numpy as np
c_x = input('Enter coeffecient of x: ')
c = input('Enter constant: ')

rhs = 25

x = 10

import numpy as np

A = np.array([ [3,-9], [2,4] ])
b = np.array([-42,2])
z = np.linalg.solve(A,b)
print(z)

M = np.array([ [1,-2,-1], [2,2,-1], [-1,-1,2] ])
c = np.array([6,1,1])
y = np.linalg.solve(M,c)
print(y)


