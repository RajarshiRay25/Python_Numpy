import numpy as np
np.random.seed(122)
arr_1=np.random.randint(1,20,9).reshape(3,3)

arr_2=np.random.randint(21,40,9).reshape(3,3)

print(f"Array 1 -> \n {arr_1}")
print(f"Array 2 -> \n {arr_2}")

#Horizontal Stacking -> Places Arrays Horizontally

Stack_Hor=np.hstack((arr_1,arr_2))

print(f"Horizontal Stacked Array -> \n {Stack_Hor}")

#Vertical Stacking -> Places Arrays Vertically

Stack_Vert=np.vstack((arr_1,arr_2))

print(f"Vertical Stacked Array -> \n {Stack_Vert}")