from turtle import pen
import numpy as np

#Using Function

arr=np.array([10,20,40,50])

plc=np.searchsorted(arr,30)
print(plc)

#Using Manuals

arr2=[]

lim=int(input("Enter Limit -> "))
Ent=int(input("Enter value to enter -> "))

i=0

for i in range(lim):
    val=int(input("Enter Values -> "))
    arr2.append(val)

arr_fin=np.array(arr2)

loc=np.searchsorted(arr_fin,Ent)

print(f"Value {Ent} placed at {loc} position")