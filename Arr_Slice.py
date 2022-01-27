import numpy as np

np.random.seed(132)

a=np.random.randint(1,200,30).reshape(5,6)

print(a[3: ,1:4])
