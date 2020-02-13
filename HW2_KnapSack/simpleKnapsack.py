import time
import matplotlib.pyplot as plt
from random import random, randint
import numpy as np


def knapsackBool(i, size):
    # knapsack is full
    if(size == 0):
        return True;
    #over full
    if(size < 0):
        return False;
    # no more objects
    if(i == 0):
        return knapsackBool(i-1, size) or knapsackBool(i-1, size -S[i])


def modifiedKnapsack(i, k1, k2):
    if(i == 0):
        return 0
    if((k2-S[i]<0) and (k1-S[i]<0)) :
        return modifiedKnapsack(i-1, k1, k2)
    if(i == 1):
        return V[i]
    if(k1 -S[i]>=0):
        return max(modifiedKnapsack(i-1,k1,k2), modifiedKnapsack(i-1, k1-S[i],k2) + V[i])
    return max(modifiedKnapsack(i-1,k1,k2), modifiedKnapsack(i-1, k1,k2-S[i]) + V[i])


def memoKnap(i, k1, k2):
    if(C[i][k1][k2] != None):
        return C[i][k1][k2]
    if(i == 0):
        rv = 0
    elif(i==1):
        rv = 0
    elif(S[i] > k2 and S[i]> k1):
        rv = memoKnap(i-1, k1, k2)
    elif (k1 - S[i] >= 0):
        rv = max(memoKnap(i - 1, k1, k2), memoKnap(i - 1, k1 - S[i], k2) + V[i])

    elif((k2-S[i] < 0) and (k1-S[i]<0)):
        rv = memoKnap(i-1, k1, k2)
    else:
        rv = max(memoKnap(i-1, k1, k2), memoKnap(i-1,k1,k2-S[i])+V[i])
    C[i][k1][k2] = rv
    return rv


def dpKnap(i, k1, k2):
    if k1 < 0 or k2 < 0:
        return float("-inf")
    if array[i][k1][k2] is not None:
        return array[i][k1][k2]
    if i == 0:
        array[i][k1][k2] = 0
        return 0
    array[i][k1][k2] = max(dpKnap(i - 1, k1, k2),dpKnap(i - 1, k1 - S[i], k2) + V[i], dpKnap(i - 1, k1, k2 - S[i]) + V[i])

    return array[i][k1][k2]


def probGen(N, aSize):
    V = [random() for x in range(0, N+1)]
    S = [randint(1, 2 * aSize) for x in range(0, N+1)]
    return S, V


K1 = 100
K2 = 100
N = 50

_memoTime = []
_size = []
_dpTime = []

for _ in range(0, 10):
    C = [[[None for k in range(0, 100 + 1)] for t in range(0, 100 + 1)] for b in range(0, N+1)]
    aSize = randint(1,2*N)
    S, V = probGen(N, aSize)
    memoTime = 0
    dpTime = 0

    for _ in range(1, 20):

        startMemo = time.time()
        memo = memoKnap(N, K1, K2)
        endMemo = time.time()
        memoTime += endMemo - startMemo

        array = np.full((N + 1, K1 + 1, K2 + 1), None)

        startDp = time.time()
        dp = dpKnap(N, K1, K2)
        endDp = time.time()
        dpTime += endDp - startDp

    _memoTime.append(memoTime)
    _dpTime.append(dpTime)
    _size.append(aSize)

plt.plot(_size, _memoTime, color='blue', label = "Memo Knapsack")
plt.plot(_size, _dpTime, color='red', label = "DP Knapsack")
plt.xlabel('Average Size')
plt.ylabel('Run Time (seconds)')
plt.title("Memoized vs Dynamic Knapsack Run Times")
plt.legend()
plt.show()
plt.savefig("test.png")

