(m, n) = map(int, input("Row x Column (m n): ").split())
g, h = (m + 2), (n + 2)
num = 0

phi = []

for i in range(g):
    size = []
    for j in range(h):
        size.append(0)
    phi.append(size)
    #print([round(a, 3) for a in phi[i]])

shape = [x[:] for x in phi]
ans = [x[:] for x in phi]

normal = input("Normal or Custom Design? (n or c): ")

if normal == 'c':
    print("\nShaping the %dx%d matrix:\n" % (m,n))
    print("[1 = Point] [2 = V1] [3 = V2] [9 = Ground]")
    for i in range(m):
        print("Include phi[%d]" % (i+1), end=":")
        shape[i + 1][1:-1] = [int(x) for x in input("").split()]

phiX = [int(x) for x in input("\nX Reference [U & D]: ").split()]
phiY = [int(x) for x in input("Y Reference [L & R]: ").split()]

for i in range(g):
    if normal == 'c':
        for j in range(h):
            phi[0][j], phi[-1][j] = phiX[0], phiX[1]
            if shape[i][j] == 9:
                phi[i][j] = phiX[1]

for i in range(m):
    phi[i + 1][0], phi[i + 1][-1] = phiY[0], phiY[1]
    if normal == 'c':
        for j in range(n + 1):
            if shape[i + 1][j] == 2:
                phi[i + 1][j] = phiY[0]
            elif shape[i + 1][j] == 3:
                phi[i + 1][j] = phiY[1]
                
for i in range(g):
        print(phi[i])
        
iter = int(input("\nNumber of iterations: "))

# 
#	X0 X0 X0
#Y0 00 01 02 Y1
#Y0 10 11 12 Y1
#	X1 X1 X1
#
# Counter clockwise
# Formula = up + left + down + right

print("\nComputed FDM:")

for k in range(iter):
    for i in range(m):
        for j in range(n):
            if normal == 'c' and shape[i + 1][j + 1] == 1:
                num += 1
                print(f"\u03A6[{num}] = ({round(phi[i][j + 1], 3)} + {round(phi[i + 1][j], 3)} + {round(phi[i + 2][j + 1],3)} + {round(phi[i + 1][j + 2],3)})/4\n")
                phi[i + 1][j + 1] = 1/4*(phi[i][j + 1] + phi[i + 1][j] + phi[i + 2][j + 1] + phi[i + 1][j + 2])
                ans[i + 1][j + 1] = "%.3f" % phi[i + 1][j + 1]
            elif normal == 'c' and shape[i + 1][j + 1] == 9:
                ans[i + 1][j + 1] = "%.3f" % phi[i + 1][j + 1]
            elif normal == 'n':
                num += 1
                print(f"\u03A6[{num}] = ({round(phi[i][j + 1], 3)} + {round(phi[i + 1][j], 3)} + {round(phi[i + 2][j + 1],3)} + {round(phi[i + 1][j + 2],3)})/4\n")
                phi[i + 1][j + 1] = 1/4*(phi[i][j + 1] + phi[i + 1][j] + phi[i + 2][j + 1] + phi[i + 1][j + 2])
                ans[i + 1][j + 1] = "%.3f" % phi[i + 1][j + 1]            
            else:
                ans[i + 1][j + 1] = "%.3f" % 0
    
    num = 0
    
    print("\nIteration ", k + 1)
    for i in range(m):
        print(ans[i + 1][1:-1], end ="\n")
        
#print(phi)