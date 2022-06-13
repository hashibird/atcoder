n, w = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
dp = [False for _ in range(w + 1)]
for i, weight1 in enumerate(weights):
  if weight1 <= w:
    dp[weight1] = True
  for j, weight2 in enumerate(weights):
    if i == j:
      break
    if weight1 + weight2 <= w:
      dp[weight1 + weight2] = True
    for k, weight3 in enumerate(weights):
      if i == k or j == k:
        break
      if weight1 + weight2 + weight3 <= w:
        dp[weight1 + weight2 + weight3] = True
  
ans = 0

for i in dp:
  if i:
    ans += 1
print(ans)