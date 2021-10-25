# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:15:52 2021

@author: Administrator
"""

(m, n) = map(int, input("Row x Column (m n): ").split())
g, h = (m + 2), (n + 2)
num = 0

order = {}
phi = []



for i in range(g):
    
    # Build Matrix of points
    size = []
    for j in range(h):
        size.append(0)
    phi.append(size)


points = int(input("Number of points to calculate: "))

for i in range(points):
    
    # Create dictionary of location for order of calculation
    num += 1
    print(f"Order {num}".rstrip())
    x, y = map(int, input("Matrix Location: ").split())
    order[i + 1] = [x, y]


print(order)

# Copying MATRIX SIZE
shape = [x[:] for x in phi]
ans = [x[:] for x in phi]



style = input("Normal or Custom Design? (n or c): ")

# Shaping the MATRIX before calculation
if style == 'c':
    print("\nShaping the %dx%d matrix:\n" % (m,n))
    print("[1 = Point] [2 = V1] [3 = V2] [9 = Ground]")
    for i in range(m):
        print("Label phi[%d]:" % (i+1))
        shape[i + 1][1:-1] = [int(x) for x in input("").split()]

# Taking given values for VOLTAGE
phiX = [float(x) for x in input("\nX Reference [U & D]: ").split()]
phiY = [float(x) for x in input("Y Reference [L & R]: ").split()]



###### BUILDING THE CUSTOM SHAPED MATRIX
for i in range(g):
    for j in range(h):
        phi[0][j], phi[-1][j] = phiX[0], phiX[1]
        if style == 'c' and shape[i][j] == 9:
            phi[i][j] = phiX[1]

for i in range(m):
    phi[i + 1][0], phi[i + 1][-1] = phiY[0], phiY[1]
    if style == 'c':
        for j in range(n + 1):
            if shape[i + 1][j] == 2:
                phi[i + 1][j] = phiY[0]
            elif shape[i + 1][j] == 3:
                phi[i + 1][j] = phiY[1]
###########################################

for i in range(g):
        print(phi[i])

#change = int(input("How many edits: "))

# for i in range(change):
#     iX, iY = map(int, input("Index: ").split())
#     phi[iX][iY] = float(input("Value: "))


iter = int(input("\nNumber of iterations: "))

print("\nComputed FDM:")

for k in range(iter):
    num = 0
    for i in range(m):
        for j in range(n):
            if style == 'c' and shape[i + 1][j + 1] == 1:
                num += 1
                p, q = order[num][0], order[num][1]
                
                print(f"\u03A6[{num}] = ({round(phi[p - 1][q], 3)} + {round(phi[p][q - 1], 3)} + {round(phi[p + 1][q],3)} + {round(phi[p][q + 1],3)})/4\n")
                phi[p][q] = 1/4*(phi[p - 1][q] + phi[p][q - 1] + phi[p + 1][q] + phi[p][q + 1])
                ans[p][q] = "%.3f" % phi[p][q]
            
            elif style == 'n':
                num += 1
                p, q = order[num][0], order[num][1]
                
                print(f"\u03A6[{num}] = ({round(phi[p - 1][q], 3)} + {round(phi[p][q - 1], 3)} + {round(phi[p + 1][q],3)} + {round(phi[p][q + 1],3)})/4\n")
                phi[p][q] = 1/4*(phi[p - 1][q] + phi[p][q - 1] + phi[p + 1][q] + phi[p][q + 1])
                ans[p][q] = "%.3f" % phi[p][q]     
            
            else:
                ans[i + 1][j + 1] = "%.3f" % 0
            
    print("\nIteration ", k + 1)
    for i in range(m):
        print(ans[i + 1][1:-1], end ="\n")