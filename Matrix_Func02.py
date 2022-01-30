import numpy as np
# np.random.seed(100)
# arr=np.random.randint(1,100,10)

arr=np.array([10,20,30,40,50,20,30,60])

print(f"Original Array -> {arr}")

#Using Shuffle Function -> Shuffles Value

np.random.shuffle(arr)

print(f"Shuffled Array -> {arr}")

#Using Unique Function -> Removes Repeated Values

print(f"Unique Array -> {np.unique(arr)}")

#Internal Functions in np.unique ->
                #return_index = True -> Returns Index Of Unique Elements
                #return_count = True -> Returns Frequency of Unique Elements

print(f"Unique Array With Index & Freq -> {np.unique(arr,return_index=True,return_counts=True)}")