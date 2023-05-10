def longest_palindromic_subsequence(s):
    n = len(s)
    L = [[0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])
    return L[0][n-1]
