import numpy as np

# Logic Searching

arr = []
# FOUND = False
i = 0
lim = int(input("Enter Limit ->"))
src = int(input("Enter Value You Want To Search ->"))


for i in range(lim):
    val = int(input("Enter Values : "))
    arr.append(val)

print(f"Array is -> {arr}")

for i in range(lim):
    if arr[i] == src:
        pos = i
        True
        if(True):
            print(f"Value {src} found at {pos} position")
    else:
        False



