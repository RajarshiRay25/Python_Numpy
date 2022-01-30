import numpy as np

# Function Search

arr=[]
i=0

lim = int(input("Enter Limit -> "))
src= int(input("Emter Element to Searrch ->"))

for i in range(lim):
    val= int(input("Enter Values -> "))
    arr.append(val)

print(f"array is -> {arr}")
arr_fin=np.array(arr)
pos = np.where(arr_fin == src)

print(f"Element {src} found at {pos} position")




