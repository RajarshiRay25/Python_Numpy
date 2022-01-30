import numpy as np
matrix =[]

row=int(input("Enter Rows ->"))
col=int(input("Enter Columns ->"))

for i in range (row):
    a=[]
    for j in range(col):
        col_val = int(input(f"Enter Values for {i} Row & {j} Col "))
        a.append(col_val)

    matrix.append(a)
arr = np.array(matrix)

for i in range(row):
    for j in range (col):
        print(arr[i][j] , end=" ")
    
    print()
