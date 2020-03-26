import numpy as np

def threeDivideConcur(n, P, Q):
    PQ = np.zeros((2*n))
    if n == 1:
        PQ[0] = P[0] * Q[0]
        return PQ
    half = int(n/2)
    PQ_LL = threeDivideConcur(half, P[0:half], Q[0:half])
    PQ_HH = threeDivideConcur(half, P[half:], Q[half:])
    P0 = [0] * half
    Q0 = [0] * half
    for i in range(half):
        P0[i] = P[i] + P[i+half]
        Q0[i] = Q[i] + Q[i+half]

    S0 = threeDivideConcur(half, P0, Q0)
    S0 = S0 - PQ_LL - PQ_HH

    for i in range(0, n):
        PQ[i] += PQ_LL[i]
        PQ[i+half] += S0[i]
        PQ[i+half] += PQ_HH[i]
    return PQ
