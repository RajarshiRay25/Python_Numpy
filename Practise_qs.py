import numpy as np

#Print a certain number n times in array

num=int(input("Enter Number -> "))

count=int(input("Enter No. Of Times ->"))


arr=np.ones(count) * num

print(f"The Array Containing {num} at {count} times is -> {arr}")

#Print Range of elements from n1 -> n2

n1=int(input("Enter First Limit ->"))
n2=int(input("Enter Final Limit ->"))

arr_range=np.arange(n1,(n2+1))

print(f"Final Array Ranged is {arr_range}")

arr_3=np.random.rand(9).reshape(3,3)
print(arr_3)
