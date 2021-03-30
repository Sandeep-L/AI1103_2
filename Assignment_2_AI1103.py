# -*- coding: utf-8 -*-
"""Assignment_2_AI1103

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I1uyPFrxOBXJRPp49qDFu-QaTZeAe76w
"""

import numpy as np
import matplotlib.pyplot as plt

def F(x):
  if (x<0):
    return 0
  elif (x>=0) and (x<1/2):
    return x/2
  elif (x>=1/2) and (x<=1):
    return x
  else:
    return 0

# x co-ordinate
X = np.linspace(0,1,100000)

# y co-ordinate
Y = [F(x) for x in X]

# Plotting
plt.plot(X,Y)
plt.grid()
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('C.D.F')
plt.show()