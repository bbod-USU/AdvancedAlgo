import matplotlib.pyplot as plt
import math
import re
import numpy as np

def main():
    with open ("../HW8/results.txt") as myFile:
        data = [line.split() for line in myFile]
    myFile.close()
    _size = []
    _time = []
    for d in data:
        _size.append(int(d[1]))
        _time.append(float(d[3]))
    plt.plot(_size, _time, color='green', label="FFT")
    plt.yscale('log')
    plt.xscale('log', basex=2)
    plt.xlabel('Highest Power')
    plt.ylabel('Run Time (seconds)')
    plt.title("FFT Algorithm")
    plt.legend()

    plt.savefig("test.png")
    plt.show()


main()