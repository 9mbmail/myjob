num = int(input("Enter size of Array:"))
'''import array
A = array.array('i',[])
for i in range(num):
    v = int(input("Enter Values"))
    A.append(v)
print(A)'''
#------------------------------------------
from array import *

B = array('f',[])
for j in range(num):
    t = float(input("Enter Values:"))
    B.append(t)
print(B)

