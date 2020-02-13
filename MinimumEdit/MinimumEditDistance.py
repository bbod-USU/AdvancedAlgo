from collections import defaultdict

def MED(i, j):
    if (i == 0):
        return j
    if (j == 0):
        return i
    return min((MED(i - 1, j) + 1), MED(i, j - 1) + 1, MED(i - 1, j - 1) + (A[i] != B[j]))

def DPmed(i,j):
    cache = [[0 for _ in range(j+1)] for _ in range(i+1)]
    for x in range(0, i+1):
        cache[x][0] = x
    for y in range(0, j+1):
        cache[0][y] = y
    for x in range(1, i+1):
        for y in range(1, j+1):
            cache[x][y] = min(cache[x-1][y]+1, cache[x][y-1]+1, cache[x-1][y-1]+(A[x] != B[y]))
    return cache[i][j]


dict = defaultdict(int)
biggestEdit = defaultdict(list)

fi = open("words.txt", "r")
for line in fi:
    l1 = line.rstrip('\r\n')
    compare = l1.split('->')
    arrayOfWords = compare[1].split(', ')
    A = compare[0]

    for word in arrayOfWords:
        B = word
        editDistance = DPmed(len(A) - 1, len(B) - 1)
        dict[editDistance] += 1
        biggestEdit[editDistance].append(A + " : " + word)
fi.close()
of = open("results.txt",'w')
largestkey=0
for key,value in dict.items():
    print(key , " : " , value, file=of)
    if key > largestkey:
        largestkey = key

print(file=of)
print("Maximal edit distance word pairs,", file=of)
print(biggestEdit[largestkey], file=of)
