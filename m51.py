def lps(string):
    n = len(string)
    # Create a 2D list to store the lengths of palindromic subsequences
    dp = [[0 for j in range(n)] for i in range(n)]
    # Base case: a single character is always a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    # Build the table bottom-up using dynamic programming
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if string[i] == string[j] and cl == 2:
                dp[i][j] = 2
            elif string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]
