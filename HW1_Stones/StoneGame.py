import sys
import time
import matplotlib.pyplot as plt
import numpy as np

N = []


def main():
    #f = open("times.txt")
    programTime = time.time()

    while time.time() - programTime < 60 * 30:
        N.append((0.0, 0.0))
        startSlowT = time.time()
        slowResult = slowWin(len(N)-1)
        slowT = time.time() - startSlowT

        startFastT = time.time()
        fastResult = fastWin(len(N)-1)
        fastT = time.time() - startFastT

        N[len(N)-1] = (slowT, fastT)
        if slowResult != fastResult:
            raise AssertionError("Values did not match up % != %" % (slowT, fastT))

    xCount = np.arange(0, len(N), 1)
    fastTimes = [n[1] for n in N]
    slowTimes = [n[0] for n in N]
    plt.subplot(221)
    plt.xlabel('Stone count')
    plt.ylabel('Seconds')
    plt.plot(xCount, slowTimes)
    plt.yscale('log')
    plt.title('Slow Recursive Algorithm')
    plt.grid(True)

    plt.subplot(222)
    plt.xlabel('Stone count')
    plt.ylabel('Seconds')
    plt.plot(xCount, fastTimes)
    plt.yscale('log')
    plt.title('Fast Memorizing Algorithm')
    plt.grid(True)
    plt.show()
    print(len(xCount))

def slowWin(n):
    if(n == 0):
        return True
    if(n == 1):
        return False
    return not(slowWin(n-1) and slowWin(n-2))


w = [None] * (len(N))

def fastWin(n):
    w.append(None)
    if(n == 0):
        return True
    if(n == 1):
        return False
    if(w[n] != None):
        return w[n]
    w[n] = not(fastWin(n-1) and fastWin(n-2))
    return w[n]

main()