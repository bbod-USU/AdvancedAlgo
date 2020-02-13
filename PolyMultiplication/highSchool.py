import numpy as np

def HighSchool(n, P, Q):
    PQ = np.zeros((2*n, 2*n))
    for i in range(0, n):
        for j in range(0, n):
            PQ[i, j] += P[i]*Q[j]

    return PQ