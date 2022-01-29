import numpy as np
arr=np.array([10,20,30,40,50])
print(f"Array is -> {arr}")
print(f"Max Element in Array is -> {np.max(arr)}")
print(f"Min Element in Array is -> {np.min(arr)}")
print(f"Max Element Position in Array is -> {np.argmax(arr)}")
print(f"Min Element Position in Array is -> {np.argmin(arr)}")
print(f"SQRT of Each Element  in Array is -> {np.sqrt(arr)}")
print(f"Sin of each Element Position in Array is -> {np.sin(arr)}")
print(f"Cos of each Element Position in Array is -> {np.cos(arr)}")

print(f"Range of values with constant gap between each number is -> {np.linspace(1,4,5)}")  #np.linspace(start,end,number of values)

