import math
import numpy as np

column_repeat = 0
row_repeat = 0
trace = 0
flag2 = 0

r = int(input('Enter some random number of rows of the matrix = '))
c = int(input('Enter some random number of columns of the matrix = '))
#case = int(input('Enter no of case='))

mtrx = []

for n in range(r):
    l = list(map(int, input('Enter elements of row separated by spaces = ').split()))
    mtrx.append(l)
    
for n in range(r):
    for m in range(c):
        if(n == m):
            trace = trace+mtrx[n][m]
            

flag1 = 0
for i in range(r) :
            for k in range(c) :
                if (i != k and mtrx[i][n] == mtrx[k][n]) :
                    row_repeat += 1
                    flag1 = 1
                    break
                
                    if (flag1 == 1):
                      break

for j in range(r) :
            for k in range(c) :
                if (j != k and mtrx[j][n] == mtrx[k][n]) :
                    column_repeat += 1
                    flag2 = 1
                    break
                    if (flag2 == 1):
                      break


print(trace,row_repeat,column_repeat)          