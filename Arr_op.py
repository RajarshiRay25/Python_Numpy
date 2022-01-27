import numpy as np
a = np.random.randint(1,200,4).reshape(2,2)
b = np.random.randint(1,200,4).reshape(2,2)
a=np.array(a)
b=np.array(b)
print(f"Array A is \n {a}")
print(f"Array B is \n {b}")
print(f"Array A + B is \n {a+b}")
print(f"Array A * B is \n {a.dot(b)}")
print(f"Array A - B is \n {a-b}")
print(f"Array A / B is \n {a/b}")

