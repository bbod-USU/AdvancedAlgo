import math
import time
import numpy as np

def saveResults(size, t):
    with open("results.txt", "a") as myfile:
        print("Size: " + str(size) + " Time: " + str(t), file=myfile)
        myfile.flush()
        myfile.close()

def getV(n, sign):
    v = []
    for j in range(0, n):
        v.append(complex(math.cos((j*2*math.pi)/n), math.sin((j*2*math.pi)/n)))
    return v if sign == 1 else conjugate(v, n)

def conjugate(v, n):
    for j in range(0, n):
        v[j] = v[j].conjugate()
    return v

def FFT(P, W, n):
    if n == 1:
        return [P[0]]
    evenP = [P[j] for j in range(0, n, 2)]
    oddP = [P[j] for j in range(1, n, 2)]
    W2 = [W[j]*W[j] for j in range(0, n//2)]
    sEven = FFT(evenP, W2, n//2)
    sOdd = FFT(oddP, W2, n//2)
    return [sEven[j]+W[j]*sOdd[j] for j in range(0, n//2)] + [sEven[j]-W[j]*sOdd[j] for j in range(0, n//2)]

def main():
    # n = 8
    # p = [0, 1, 2, 3, 4, 5, 6, 7]
    # print("Forward FFT")
    # sol = FFT([complex(p[i], 0) for i in range(0, n)], getV(n, +1), n)
    # print(sol)
    # print("Inverse FFT")
    # back = [s / 8 for s in FFT(sol, getV(n, -1), n)]
    # print("Answer")
    # print(back)
    pow2 = []
    for i in range(7, 55):
        pow2.append(2 ** i)
    for n in pow2:
        P = np.arange(n)
        start = time.time()
        sol = FFT([complex(P[i], 0) for i in range(0, n)], getV(n, +1), n)
        stop = time.time()
        #inverseSol = FFT([complex(P[i], 0) for i in range(0, n)], getV(n, +1), n)
        saveResults(n, stop-start)
main()