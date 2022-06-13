"""
2 10
3 6
4 5

"""

import collections
 
N, X = map(int, input().split())
dp = [collections.defaultdict(int) for _ in range(N + 1)]
dp[0][0] = 1

 
for i in range(N):
    a, b = map(int, input().split())
    for j in dp[i].keys():
        dp[i + 1][j + a] = 1
        dp[i + 1][j + b] = 1
print(dp)
 
print(["No", "Yes"][dp[N][X]])