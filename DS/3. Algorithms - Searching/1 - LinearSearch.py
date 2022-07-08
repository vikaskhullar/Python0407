def linearSearch(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:
            return i
    
    return -1


import numpy as np
a = np.arange(100000)
a

np.random.shuffle(a)
a

linearSearch(a,99999)




import math 
math.log2(10)

