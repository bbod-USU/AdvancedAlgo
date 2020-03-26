

def dpLCS(s1, s2):
    letters = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                letters[i][j]=0
            elif s1[i-1] == s2[j-1]:
                letters[i][j] = letters[i-1][j-1]+1
            else:
                letters[i][j] = max(letters[i-1][j], letters[i][j-1])

    return letters[len(s1)][len(s2)]

def LCS(s1, s2):
    longest = 0
    if len(s1) == 0 or len(s2) == 0:
        return longest

    if(s1[0] == s2[0]):
        longest += 1
        longest += LCS(s1[1:], s2[1:])
        return longest
    longest += max(LCS(s1[1:], s2), LCS(s1, s2[1:]))

    return longest

def dpChange(c):
    S = [0]*(c+1)
    S[0] = 0
    for i in range (1,c+1):
        x = S[i-1]
        if i-7 >= 0:
            x=min(S[i-7],x)
        if i -27 >= 0:
            x = min(S[i-27], x)
        S[i] = x+1
    return S[c]

def main():
    print(LCS("AGGTAB", "GXTXAYB"))
    print (dpLCS("AGGTAB","GXTXAYB"))
    print(dpChange(10))
main()