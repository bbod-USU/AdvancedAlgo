import numpy as np

def DivideConcur(n, P, Q):
    PQ = np.zeros((2*n))
    if n == 1:
        PQ[0] = P[0] * Q[0]
        return PQ
    half = int(n/2)
    PQ_LL = DivideConcur(half, P[0:half], Q[0:half])
    PQ_HH = DivideConcur(half, P[half:], Q[half:])
    PQ_LH = DivideConcur(half, P[0:half], Q[half:])
    PQ_HL = DivideConcur(half, P[half:], Q[0:half])

    for i in range(0, n):
        PQ[i] += PQ_LL[i]
        PQ[i+half] += PQ_LH[i]
        PQ[i+half] += PQ_HL[i]
        PQ[i+half] += PQ_HH[i]
    return PQ
