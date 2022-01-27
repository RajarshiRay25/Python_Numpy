import numpy as np
a=[]
sum=0
limit=int(input("Enter Limit -->"))
for i in range(limit):
    val=int(input(f"Enter Values for {i} position -->"))
    sum=sum+val
    a.append(val)

arr_final=np.array(a)
arr_slice = arr_final[2:4]
print(arr_final)
print(f"sum is {sum}")
print(arr_slice)

