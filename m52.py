def largest_submatrix(M):
    m, n = len(M), len(M[0])
    S = [[0] * n for _ in range(m)]
    
    # initialize first row and column
    for i in range(m):
        S[i][0] = M[i][0]
    for j in range(n):
        S[0][j] = M[0][j]
        
    # fill in the rest of S
    max_size = 0
    for i in range(1, m):
        for j in range(1, n):
            if M[i][j] == 1:
                S[i][j] = min(S[i-1][j], S[i][j-1], S[i-1][j-1]) + 1
                max_size = max(max_size, S[i][j])
                
    # extract submatrix from M
    for i in range(m):
        for j in range(n):
            if S[i][j] == max_size:
                return [M[x][j-max_size+1:j+1] for x in range(i-max_size+1,i+1)]
