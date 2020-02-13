import time
import random
import numpy as np
random.seed(time.time())
def GenerateProblem(size):
    returnValues = np.zeros(size*32)
    for i in range(size*32):
        returnValues[i] = random.uniform(-1, 1)
    return returnValues
