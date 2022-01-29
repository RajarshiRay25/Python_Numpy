from turtle import pen
from matplotlib.pyplot import axis
import numpy as np
np.random.seed(122)
matrix=np.random.randint(10,100,9).reshape(3,3)
print(f"The matrix is -> \n {matrix} ")

Min_matrix=np.min(matrix)

print(f"Min value of the Matrix is -> \n {Min_matrix}")

Cumulative_sum=np.cumsum(matrix)

print(f"Cumulative Sum is -> {Cumulative_sum}")

#Row Wise Operations ->
#Row is denoted as (axis = 1)

Min_matrix_row=np.min(matrix,axis=1)
print(f"Min Value of the Matrix Row wise is -> \n {Min_matrix_row}")  #Finds the Min values of each row

Max_matrix_row=np.max(matrix,axis=1)
print(f"Max Value of the Matrix Row wise is -> \n {Max_matrix_row}")  #Finds the Max values of each row

Sum_matrix_row=np.sum(matrix,axis=1)

print(f"Sum of Row wise matrix values -> \n {Sum_matrix_row}")        #Finds Sum of row wise

#Similarly sqrt,sin,cos etc can be used

#Column Wise Operations ->
#Column is denoted as (axis = 0)

Min_matrix_col=np.min(matrix,axis=0)
print(f"Min Value of the Matrix Col wise is -> \n {Min_matrix_col}")  #Finds the Min values of each col

Max_matrix_col=np.max(matrix,axis=0)
print(f"Max Value of the Matrix Col wise is -> \n {Max_matrix_col}")  #Finds the Max values of each col

Sum_matrix_col=np.sum(matrix,axis=0)
print(f"Sum of Col wise matrix values -> \n {Sum_matrix_col}")        #Finds Sum of col wise

#Similarly sqrt,sin,cos etc can be used