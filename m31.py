def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # initialize the LCS array with zeros
    LCS = [[0 for j in range(n+1)] for i in range(m+1)]
    # variable to store the length of the longest common substring
    longest = 0
    # variable to store the ending position of the longest common substring in X
    ending_pos = 0
    # fill the LCS array using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
                if LCS[i][j] > longest:
                    longest = LCS[i][j]
                    ending_pos = i
            else:
                LCS[i][j] = 0
    # extract the longest common substring from X
    start_pos = ending_pos - longest
    return X[start_pos:ending_pos]
