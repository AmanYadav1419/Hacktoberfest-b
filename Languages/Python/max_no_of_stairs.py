# Python3 function to calculate number of possible stairs arrangements with given number of boxes/bricks

def solution(n):
    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]
    for i in range(n+1):
        for j in range (n+1):
            dp[i][j]=0
    dp[3][2]=1
    dp[4][2]=1
    for i in range(5,n+1):
        for j in range(2,i+1):
            dp[i][j] = dp[i-j][j] + 1 if (j == 2) else (dp[i-j][j] + dp[i-j][j - 1])
    return sum(dp[n][i] for i in range (1, n+1))

print(solution(3))
